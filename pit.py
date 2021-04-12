import arena
from mcts import MCTS
from game import Game
from player_types import *
from neural_net import NNetWrapper as NNet

import numpy as np


"""
use this script to play any two agents against each other, or play manually with
any agent.
"""



# Initialize nodes
number_of_nodes = 5
# Original number of nodes
# number_of_nodes = 199

# Initialize edges
edges = [(0, 1, {"type": "taxi"}),
         (1, 2, {"type": "taxi"}),
         (2, 0, {"type": "taxi"}),
         (3, 4, {"type": "bus"}),
         (3, 4, {"type": "taxi"}),
         (3, 4, {"type": "metro"}),
         (3, 2, {"type": "ferry"}),
         (0, 4, {"type": "taxi"}),
         (1, 3, {"type": "taxi"}),
         (2, 4, {"type": "taxi"})]

edges_2 = [(0, 1, {"type": "ferry"}),
           (1, 2, {"type": "ferry"}),
           (2, 0, {"type": "ferry"}),
           (3, 4, {"type": "ferry"}),
           (0, 4, {"type": "ferry"}),
           (1, 3, {"type": "ferry"}),
           (2, 4, {"type": "ferry"}),
           (3, 1, {"type": "ferry"})]

# Assign colors and widths to edges for visualization
for edge in edges:
    edge_attributes = edge[2]
    if edge_attributes["type"] == 'taxi':
        edge_color = (255 / 255, 205 / 255, 66 / 255)
        edge_width = 10.0
    elif edge_attributes["type"] == 'bus':
        edge_color = (23 / 255, 160 / 255, 93 / 255)
        edge_width = 6.0
    elif edge_attributes["type"] == 'metro':
        edge_color = (221 / 255, 80 / 255, 68 / 255)
        edge_width = 3.0
    elif edge_attributes["type"] == "ferry":
        edge_color = 'black'
        edge_width = 0.5
    else:
        edge_color = 'black'
        edge_width = 10.0

    edge_attributes["color"] = edge_color
    edge_attributes["width"] = edge_width

# Initialize players
number_of_detectives = 2

# Set the colors for the different roles (for visualization purposes)
detective_colors = ['green', 'red']
mister_x_color = 'grey'
game = Game(number_of_nodes, edges, number_of_detectives, mister_x_color, detective_colors)


# Players for Mister X
#random_player = RandomPlayer(game).play
#greedy_player = GreedyPlayer(game).play
human_player = HumanPlayer(game).play
neural_net_mister_x = NNet(game, is_mister_x=True)
# neural_net_player.load_checkpoint('')

args1 = dict({'numMCTSSims': 50, 'cpuct': 1.0})
mcts1 = MCTS(game, neural_net_mister_x, args1)
n1p = lambda x, y: np.argmax(mcts1.get_action_prob(x, y, temp=0))

"""human_vs_cpu = False
if human_vs_cpu:
    player2 = human_player
else:
    n2 = NNet(game)
    #n2.load_checkpoint('')
    args2 = dict({'numMCTSSims': 50, 'cpuct': 1.0})
    mcts2 = MCTS(game, n2, args2)
    n2p = lambda x: np.argmax(mcts2.get_action_prob(x, temp=0))

    player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.
"""
neural_net_detectives = []
neural_net_detective = NNet(game, is_mister_x=False)
# n2.load_checkpoint('')
args2 = dict({'numMCTSSims': 50, 'cpuct': 1.0})
mcts2 = MCTS(game, neural_net_detective, args2)
n2p = lambda x, y: np.argmax(mcts2.get_action_prob(x, y, temp=0))
for i in range(number_of_detectives):
    neural_net_detectives.append(n2p)

arena = arena.Arena(n1p, neural_net_detectives, game, display=game.display)

#print(arena.play_games(2, verbose=True))
print(arena.play_game(verbose=True))
