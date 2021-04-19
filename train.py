import logging

from Coach import Coach
from game import Game
from neural_net import NNetWrapper as NNet
from utils import *

log = logging.getLogger(__name__)

args = dict({
    'numIters': 1000,
    'numEps': 100,              # Number of complete self-play games to simulate during a new iteration.
    'tempThreshold': 15,        #
    'updateThreshold': 0.6,     # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    'maxlenOfQueue': 200000,    # Number of game examples to train the neural networks.
    'numMCTSSims': 25,          # Number of games moves for MCTS to simulate.
    'arenaCompare': 40,         # Number of games to play during arena play to determine if new net will be accepted.
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': False,
    'load_folder_file': ('/dev/models/8x100x50','best.pth.tar'),
    'numItersForTrainExamplesHistory': 20,

})


def main():
    log.info('Loading Game')
    number_of_nodes = 5
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

    neural_net_mister_x = NNet(game, player=game.mister_x)
    game.mister_x.neural_net = neural_net_mister_x
    neural_net_detective = NNet(game, game.detectives[0])
    for detective in game.detectives:
        detective.neural_net = neural_net_detective
    """if args['load_model']:
        log.info('Loading checkpoint "%s/%s"...', args['load_folder_file'])
        nnet.load_checkpoint(args['load_folder_file'][0], args['load_folder_file'][1])
    else:
        log.warning('Not loading a checkpoint!')
    """

    log.info('Loading the Coach...')
    c = Coach(game, neural_net_mister_x, neural_net_detective, args)

    """if args['load_model']:
        log.info("Loading 'trainExamples' from file...")
        c.loadTrainExamples()
    """

    log.info('Starting the learning process 🎉')
    c.learn()


if __name__ == "__main__":
    main()
