import logging

from tqdm import tqdm

log = logging.getLogger(__name__)


class Arena:
    """
    An Arena class where any 2 agents can be pit against each other.
    """

    def __init__(self, mister_x, detectives, game, display=None):
        """
        Input:
            player 1,2: two functions that takes board as input, return action
            game: Game object
            display: a function that takes board as input and prints it (e.g.
                     display in othello/OthelloGame). Is necessary for verbose
                     mode.

        see othello/OthelloPlayers.py for an example. See pit.py for pitting
        human players/other baselines with each other.
        """
        self.mister_x = mister_x
        self.detectives = detectives
        self.game = game
        self.display = display

    def play_game(self, verbose=False):
        """
        Executes one episode of a game.

        Returns:
            either
                winner: player who won the game (1 if mister X, -1 if detectives)
            or
                draw result returned from the game that is neither 1, -1, nor 0.
        """

        players = [self.mister_x] + self.detectives
        cur_player_index = 0
        cur_player_name = self.game.players[cur_player_index].name
        current_player = self.game.players[cur_player_index]
        board = self.game.get_init_board()
        it = 0
        while self.game.is_game_over(verbose=1) == 0:
            it += 1
            if verbose:
                assert self.display
                print("Turn ", str(it), "Player ", str(cur_player_index))
                self.display()

            canon_board = self.game.get_canonical_form(board, current_player)
            action = players[cur_player_index](self.game.get_canonical_form(board, current_player), current_player)

            valids = self.game.get_valid_moves(current_player)

            if valids[action] == 0:
                log.error(f'Action {action} is not valid!')
                log.debug(f'valids = {valids}')
                assert valids[action] > 0
            board, cur_player_index = self.game.get_next_state(board, cur_player_index, action)
        if verbose:
            assert self.display
            print("Game over: Turn ", str(it), "Result ", str(self.game.get_game_ended(board, 1)))
            self.display(board)
        return cur_player_index * self.game.get_game_ended(board, cur_player_index)

    def play_games(self, num, verbose=False):
        """
        Plays num games in which player1 starts num/2 games and player2 starts
        num/2 games.

        Returns:
            oneWon: games won by player1
            twoWon: games won by player2
            draws:  games won by nobody
        """

        num = int(num / 2)
        oneWon = 0
        twoWon = 0
        draws = 0
        for _ in tqdm(range(num), desc="Arena.playGames (1)"):
            gameResult = self.play_game(verbose=verbose)
            if gameResult == 1:
                oneWon += 1
            elif gameResult == -1:
                twoWon += 1
            else:
                draws += 1

        self.player1, self.player2 = self.player2, self.player1

        for _ in tqdm(range(num), desc="Arena.playGames (2)"):
            gameResult = self.play_game(verbose=verbose)
            if gameResult == -1:
                oneWon += 1
            elif gameResult == 1:
                twoWon += 1
            else:
                draws += 1

        return oneWon, twoWon, draws
