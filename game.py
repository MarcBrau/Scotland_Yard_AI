from mister_x import MisterX
from detective import Detective
from board import Board
from utils.draw_graph import *
import random
import numpy as np


class Game:

    def __init__(self, number_of_nodes, edges, num_detectives, mister_x_color, detective_color):

        # Initialize players
        # Create pools of starting positions
        # Todo: Search correct starting positions
        # self.starting_positions_mister_x = [0, 1]
        self.starting_positions_mister_x = [3]
        # self.starting_positions_detectives = [2, 3, 4]
        self.starting_positions_detectives = [2, 1]

        self.mister_x, self.detectives = self.initialize_players(mister_x_color, detective_color, num_detectives)
        self.players = self.detectives.copy()
        self.players.insert(0, self.mister_x)

        # Initialize board
        self.num_nodes = number_of_nodes
        # Todo: Make nodes from 1 to ... not 0 to ...number_of_nodes-1
        self.node_indices = list(range(self.num_nodes))

        node_positions = {}
        # Todo: Find more sophisticated way of calculating fixed screen positions for drawing
        for node_index in self.node_indices:
            if node_index <= len(self.node_indices) / 2:
                node_positions[node_index] = [node_index / (len(self.node_indices) / 2), 0]
            else:
                node_positions[node_index] = [
                    (node_index - (len(self.node_indices) / 2)) / (len(self.node_indices) / 2), 1]

        # Todo: Find better way for node type, is it even needed?!
        # occupied = 1: Mister X's node, -1: Detective's node, 0: unoccupied
        self.nodes = [(node_index, {"position": node_positions[node_index], "type": "no_type", "occupied": 0}) for node_index in
                      self.node_indices]
        self.edges = edges

        self.board = Board(self.nodes, self.edges)

        self.num_edges = len(edges)
        self.num_edges_detectives = self.board.detectives_network.number_of_edges()

        # Connect board and players
        for player in self.players:
            player_position = player.get_position()
            if player.name == "Mister_X":
                new_attribute = {player_position: {"occupied": 1}}
                nx.set_node_attributes(self.board.mister_x_network, values=new_attribute)
            else:
                new_attribute = {player_position: {"occupied": -1}}
                nx.set_node_attributes(self.board.mister_x_network, values=new_attribute)

        # Initialize round index
        self.round_index = 0

    def initialize_players(self, mister_x_color, detective_colors, num_detectives=1):
        # Todo:
        # Todo: Make documentation using this comment
        #  Choose random starting positions of players, drawn from the respective pool of starting position

        # Initialize Mister X
        start_pos_mister_x = random.choice(self.starting_positions_mister_x)
        mister_x = MisterX(start_position=start_pos_mister_x, color=mister_x_color)

        # Initialize detectives
        detectives = []
        for detective_index in range(num_detectives):
            start_pos_detective = random.choice(self.starting_positions_detectives)
            # Initialize detective using the start position
            detective = Detective(index=detective_index, start_position=start_pos_detective, color=detective_colors[detective_index])
            detectives.append(detective)
            # Remove start position from the current detective from the pool of start positions to guarantee unique
            # start positions
            self.starting_positions_detectives.remove(start_pos_detective)

        return mister_x, detectives

    def get_init_board(self):
        # return initial board
        init_board = Board(self.nodes, self.edges)
        return init_board

    def string_representation(self, board):
        #return str(board.adj)
        return str(board)

    """def play_game(self, move_by_human=False):

        while True:
            self.round_index += 1

            # Get status
            print(self.get_status(self.mister_x, self.detectives))

            # Draw board and players
            draw_graph_and_players(self.board.mister_x_network, self.mister_x, self.detectives, by_human=move_by_human)

            # Check if Mister X was caught
            if self.is_game_over():
                break

            # Get valid moves
            self.get_valid_moves(self.mister_x)

            # Move Mister X
            self.board.move_mister_x(self.mister_x, self.detectives, by_human=move_by_human)

            # Move detectives
            self.board.move_detectives(self.detectives, by_human=move_by_human)

        # Todo: Create game history/summary (Moves of players, used tickets, ...)
        """

    def get_status(self, mister_x, detectives):
        status_x = mister_x.get_status()
        status_detectives = ""
        for detective in detectives:
            status_detective = detective.get_status()
            status_detectives += "\n" + status_detective
        status_game = "Status game: \n" \
                      "Current round: {} \n".format(self.round_index)
        status = status_game + "\n" + status_x + "\n" + status_detectives
        return status

    def is_game_over(self, verbose=0):
        """
        Return 1 if mister_x won, -1 if detectives won, 0 if game is not over
        :param verbose:
        :return:
        """
        # Todo: Set correct conditions to end the game
        if self.round_index == 24:
            if verbose:
                print("Mister X accomplished to escape for {} rounds and thus won the game.".format(self.round_index))
            return 1
        for detective in self.detectives:
            if self.mister_x.get_position() == detective.get_position():
                if verbose:
                    print("Mister X was caught in round {} on position {} by detective {}"
                          .format(self.round_index, self.mister_x.get_position(), detective.get_index()))
                return -1
        return 0

    def get_canonical_form(self, board, current_player):
        canon_form = [0] * len(board.mister_x_network.nodes)

        # Todo: Find good way for detectives when Mister X is not visible
        # if current_player.name == "Mister_X":
        for player in self.players:
            if player.name != current_player.name:
                canon_form[player.position] = 1

        return np.array(canon_form)

    def get_symmetries(self, board, pi, player):
        return [(board,pi)]

    def get_valid_moves(self, player):
        """

        :return: Fixed size binary vector
        """

        # Get the indices of all neighboring nodes of the player
        neighbors, connection_types = self.board.get_neighbors(player)
        # From the neighbors, delete all which cannot be reached
        valid_neighbors, valid_connection_types = self.board.get_valid_neighbors(player, self.detectives, neighbors, connection_types)

        # Create a binary vector indicating the valid edges
        valid_moves = self.board.get_valid_edges(player, valid_neighbors)
        # Todo: what happens when there are no valid moves
        return np.array(valid_moves)

    def get_action_size(self, player):
        """
        Used to define the number of neurons in the output layer of the neural network
        :return:
        """
        if player.name == "Mister_X":
            return self.num_edges
        else:
            return self.num_edges_detectives

    def get_board_size(self):
        return self.num_nodes

    def get_next_state(self, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        # Todo: Think about this, what's the purpose?:
        # if action == self.n*self.n:
        #    return (board, -player)

        self.board.move_player(action, player)
        # Todo: How to get next player, outside of this routine, something like:
        # for player in players:
        # get_next_state(player, action)...
        curr_index = self.players.index(player)
        if curr_index == len(self.players) - 1:
            curr_index = -1
        next_player = self.players[curr_index + 1]
        return self.board, next_player

    def display(self):
        draw_graph_and_players(self.board.mister_x_network, self.mister_x, self.detectives, by_human=False)
