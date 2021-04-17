import numpy as np
import math

EPS = 1e-8

# Todo: Use a good logger instead of print
# log = logging.getLogger(__name__)


class MCTS:
    """
        This class handles the MCTS tree.
        """

    def __init__(self, game, neural_net, args):
        self.game = game
        self.neural_net = neural_net
        self.args = args
        self.q_values_s_a = {}  # stores Q values for s,a (as defined in the paper)
        self.num_s_a = {}  # stores #times edge s,a was visited
        self.num_s = {}  # stores #times board s was visited
        self.nnet_policy_s = {}  # stores initial policy (returned by neural net)

        self.Es = {}  # stores game.getGameEnded ended for board s
        self.Vs = {}  # stores game.getValidMoves for board s

    def get_action_prob(self, canonical_board, current_player, temp=1):
        """
        This function performs numMCTSSims simulations of MCTS starting from
        canonical_board.

        Returns:
            probs: a policy vector where the probability of the ith action is
                   proportional to num_s_a[(s,a)]**(1./temp)
        """
        for i in range(self.args['numMCTSSims']):
            self.search(canonical_board, current_player)

        s = self.game.string_representation(canonical_board)
        counts = [self.num_s_a[(s, a)] if (s, a) in self.num_s_a else 0 for a in range(self.game.getActionSize())]

        if temp == 0:
            bestAs = np.array(np.argwhere(counts == np.max(counts))).flatten()
            bestA = np.random.choice(bestAs)
            probs = [0] * len(counts)
            probs[bestA] = 1
            return probs

        counts = [x ** (1. / temp) for x in counts]
        counts_sum = float(sum(counts))
        probs = [x / counts_sum for x in counts]
        return probs

    def search(self, canonicalBoard, current_player):
        """
        This function performs one iteration of MCTS. It is recursively called
        till a leaf node is found. The action chosen at each node is one that
        has the maximum upper confidence bound as in the paper.

        Once a leaf node is found, the neural network is called to return an
        initial policy P and a value v for the state. This value is propagated
        up the search path. In case the leaf node is a terminal state, the
        outcome is propagated up the search path. The values of num_s, num_s_a, q_values_s_a are
        updated.

        NOTE: the return values are the negative of the value of the current
        state. This is done since v is in [-1,1] and if v is the value of a
        state for the current player, then its value is -v for the other player.

        Returns:
            v: the negative of the value of the current canonical_board
        """

        s = self.game.string_representation(canonicalBoard)

        if s not in self.Es:
            self.Es[s] = self.game.is_game_over(verbose=1)
        if self.Es[s] != 0:
            # terminal node
            return -self.Es[s]

        if s not in self.nnet_policy_s:
            # leaf node
            self.nnet_policy_s[s], v = self.neural_net.predict(canonicalBoard)
            valids = self.game.get_valid_moves(current_player)
            self.nnet_policy_s[s] = self.nnet_policy_s[s] * valids  # masking invalid moves
            sum_Ps_s = np.sum(self.nnet_policy_s[s])
            if sum_Ps_s > 0:
                self.nnet_policy_s[s] /= sum_Ps_s  # renormalize
            else:
                # if all valid moves were masked make all valid moves equally probable

                # NB! All valid moves may be masked if either your NNet architecture is insufficient or you've get overfitting or something else.
                # If you have got dozens or hundreds of these messages you should pay attention to your NNet and/or training process.
                # log.error("All valid moves were masked, doing a workaround.")
                print("All valid moves were masked, doing a workaround.")
                self.nnet_policy_s[s] = self.nnet_policy_s[s] + valids
                self.nnet_policy_s[s] /= np.sum(self.nnet_policy_s[s])

            self.Vs[s] = valids
            self.num_s[s] = 0
            return -v

        valids = self.Vs[s]
        cur_best = -float('inf')
        best_act = -1

        # pick the action with the highest upper confidence bound
        for a in range(self.game.get_action_size(current_player.name)):
            if valids[a]:
                if (s, a) in self.q_values_s_a:
                    u = self.q_values_s_a[(s, a)] + self.args['cpuct'] * self.nnet_policy_s[s][a] * math.sqrt(self.num_s[s]) / (
                            1 + self.num_s_a[(s, a)])
                else:
                    u = self.args['cpuct'] * self.nnet_policy_s[s][a] * math.sqrt(self.num_s[s] + EPS)  # Q = 0 ?

                if u > cur_best:
                    cur_best = u
                    best_act = a

        a = best_act
        next_s, next_player = self.game.get_next_state(current_player, a)
        next_s = self.game.get_canonical_form(next_s, next_player)

        v = self.search(next_s, next_player)

        if (s, a) in self.q_values_s_a:
            self.q_values_s_a[(s, a)] = (self.num_s_a[(s, a)] * self.q_values_s_a[(s, a)] + v) / (self.num_s_a[(s, a)] + 1)
            self.num_s_a[(s, a)] += 1

        else:
            self.q_values_s_a[(s, a)] = v
            self.num_s_a[(s, a)] = 1

        self.num_s[s] += 1
        return -v
