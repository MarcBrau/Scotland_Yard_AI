import logging
import os
import sys
from collections import deque
from pickle import Pickler, Unpickler
from random import shuffle

import numpy as np
from tqdm import tqdm

from arena import Arena
from mcts import MCTS

log = logging.getLogger(__name__)


class Coach:
    """
    This class executes the self-play + learning. It uses the functions defined
    in Game and NeuralNet. args are specified in main.py.
    """

    def __init__(self, game, neural_net_mister_x, neural_net_detectives, args):
        self.game = game
        self.nnet = neural_net_mister_x
        # self.pnet = self.nnet.__class__(self.game)  # the competitor network
        self.pnet = neural_net_detectives  # the competitor network
        self.args = args
        self.mcts_mister_x = MCTS(self.game, self.nnet, self.args)
        self.mcts_detectives = MCTS(self.game, self.pnet, self.args)
        self.train_examples_history = []  # history of examples from args.numItersForTrainExamplesHistory latest iterations
        self.skipFirstSelfPlay = False  # can be overriden in loadTrainExamples()

    def execute_episode(self):
        """
        This function executes one episode of self-play, starting with player 1.
        As the game is played, each turn is added as a training example to
        trainExamples. The game is played till the game ends. After the game
        ends, the outcome of the game is used to assign values to each example
        in trainExamples.

        It uses a temp=1 if episodeStep < tempThreshold, and thereafter
        uses temp=0.

        Returns:
            trainExamples: a list of examples of the form (canonical_board, currPlayer, pi,v)
                           pi is the MCTS informed policy vector, v is +1 if
                           the player eventually won the game, else -1.
        """
        trainExamples = []
        # board = self.game.get_init_board()
        board = self.game.board
        cur_player_index = 0
        self.current_player = self.game.players[cur_player_index]
        episodeStep = 0

        while True:
            episodeStep += 1
            canonical_board = self.game.get_canonical_form(board, self.current_player)
            temp = int(episodeStep < self.args['tempThreshold'])

            pi = self.mcts.get_action_prob(canonical_board, self.current_player, temp=temp)
            sym = self.game.get_symmetries(canonical_board, pi, self.current_player)
            for b, p in sym:
                trainExamples.append([b, self.current_player, p, None])

            action = np.random.choice(len(pi), p=pi)
            board, self.current_player = self.game.get_next_state(self.current_player, action)

            r = self.game.is_game_over()

            if r != 0:
                return [(x[0], x[2], r * ((-1) ** (x[1] != self.current_player))) for x in trainExamples]

    def learn(self):
        """
        Performs numIters iterations with numEps episodes of self-play in each
        iteration. After every iteration, it retrains neural network with
        examples in trainExamples (which has a maximum length of maxlenofQueue).
        It then pits the new neural network against the old one and accepts it
        only if it wins >= updateThreshold fraction of games.
        """

        for i in range(1, self.args['numIters'] + 1):
            # bookkeeping
            log.info(f'Starting Iter #{i} ...')
            # examples of the iteration
            if not self.skipFirstSelfPlay or i > 1:
                iteration_train_examples = deque([], maxlen=self.args['maxlenOfQueue'])

                for _ in tqdm(range(self.args['numEps']), desc="Self Play"):
                    self.mcts = MCTS(self.game, self.nnet, self.args)  # reset search tree
                    iteration_train_examples += self.execute_episode()

                # save the iteration examples to the history
                self.train_examples_history.append(iteration_train_examples)

            if len(self.train_examples_history) > self.args['numItersForTrainExamplesHistory']:
                log.warning(
                    f"Removing the oldest entry in trainExamples. len(trainExamplesHistory) = {len(self.train_examples_history)}")
                self.train_examples_history.pop(0)
            # backup history to a file
            # NB! the examples were collected using the model from the previous iteration, so (i-1)
            self.save_train_examples(i - 1)

            # shuffle examples before training
            trainExamples = []
            for e in self.train_examples_history:
                trainExamples.extend(e)
            shuffle(trainExamples)

            # training new network, keeping a copy of the old one
            self.nnet.save_checkpoint(folder=self.args['checkpoint'], filename='temp.pth.tar')
            self.pnet.load_checkpoint(folder=self.args['checkpoint'], filename='temp.pth.tar')
            pmcts = MCTS(self.game, self.pnet, self.args)

            self.nnet.train(trainExamples)
            nmcts = MCTS(self.game, self.nnet, self.args)

            log.info('PITTING AGAINST PREVIOUS VERSION')
            arena = Arena(lambda x, y: np.argmax(pmcts.get_action_prob(x, y, temp=0)),
                          lambda x, y: np.argmax(nmcts.get_action_prob(x, y, temp=0)), self.game)
            pwins, nwins, draws = arena.play_games(self.args['arenaCompare'])

            log.info('NEW/PREV WINS : %d / %d ; DRAWS : %d' % (nwins, pwins, draws))
            if pwins + nwins == 0 or float(nwins) / (pwins + nwins) < self.args['updateThreshold']:
                log.info('REJECTING NEW MODEL')
                self.nnet.load_checkpoint(folder=self.args['checkpoint'], filename='temp.pth.tar')
            else:
                log.info('ACCEPTING NEW MODEL')
                self.nnet.save_checkpoint(folder=self.args['checkpoint'], filename=self.get_checkpoint_file(i))
                self.nnet.save_checkpoint(folder=self.args['checkpoint'], filename='best.pth.tar')

    def get_checkpoint_file(self, iteration):
        return 'checkpoint_' + str(iteration) + '.pth.tar'

    def save_train_examples(self, iteration):
        folder = self.args['checkpoint']
        if not os.path.exists(folder):
            os.makedirs(folder)
        filename = os.path.join(folder, self.get_checkpoint_file(iteration) + ".examples")
        with open(filename, "wb+") as f:
            Pickler(f).dump(self.train_examples_history)
        f.closed

    def load_train_examples(self):
        modelFile = os.path.join(self.args['load_folder_file'][0], self.args['load_folder_file'][1])
        examplesFile = modelFile + ".examples"
        if not os.path.isfile(examplesFile):
            log.warning(f'File "{examplesFile}" with trainExamples not found!')
            r = input("Continue? [y|n]")
            if r != "y":
                sys.exit()
        else:
            log.info("File with trainExamples found. Loading it...")
            with open(examplesFile, "rb") as f:
                self.train_examples_history = Unpickler(f).load()
            log.info('Loading done!')

            # examples based on the model were already collected (loaded)
            self.skipFirstSelfPlay = True
