from mister_x import MisterX
from detective import Detective
import networkx as nx
import random


class Board:
    """
    This class represents one transportation network consisting of nodes and edges.
    """

    def __init__(self, nodes, edges, players):
        """
        Init-function of the Board-class.
        :param nodes: List of nodes which are part of the network
        :param edges: List of edges connecting the nodes given as first argument
        """

        # Initialize different networks
        self.mister_x_network = nx.MultiGraph(name="mister_x_network")
        mister_x_nodes = [node for node in nodes]
        mister_x_edges = [edge for edge in edges]

        self.mister_x_network.add_nodes_from(mister_x_nodes)
        self.mister_x_network.add_edges_from(mister_x_edges)

        self.detectives_network = nx.MultiGraph(name="detectives_network")
        detectives_nodes = [node for node in nodes if node[1]["type"] != "ferry"]
        detectives_edges = [edge for edge in edges if edge[2]["type"] != "ferry"]
        self.detectives_network.add_nodes_from(detectives_nodes)
        self.detectives_network.add_edges_from(detectives_edges)

        self.networks = [self.mister_x_network, self.detectives_network]

        """self.pieces = [0] * len(nodes)
        for player in players:
            if player.name is "Mister_X":
                self.pieces[player.get_position()] = 1
            else:
                self.pieces[player.get_position()] = -1

        self.init_pieces = self.pieces"""

    def move_mister_x(self, mister_x, detectives, by_human=False):
        # Get neighbors of mister X's node
        neighbors, connection_types = self.get_neighbors(mister_x)

        # Get all valid neighbors
        valid_neighbors, valid_connection_types = self.get_valid_neighbors(mister_x, detectives, neighbors, connection_types)

        # Calculate distances to the detectives
        distances, shortest_paths, transportation_types = self.calculate_shortest_paths(mister_x, detectives)

        # Get estimate of the policy from neural net

        # Determine position where Mister X should move
        best_position = valid_neighbors[0]
        connection_type = valid_connection_types[0]

        if by_human:
            valid_input = False
            while not valid_input:
                player_input = input("Input position to which Mister X should move: ")
                try:
                    player_input = int(player_input)
                except Exception:
                    print("Invalid input, not a valid position")
                    continue
                if player_input in valid_neighbors:
                    valid_input = True
                    best_position = player_input
                    input_index = valid_neighbors.index(best_position)
                    connection_type = valid_connection_types[input_index]
                    print("Valid input, Mister X moved to position {}".format(best_position))
                else:
                    valid_input = False
                    print("Invalid input, please try again")

        # Move Mister X
        mister_x.move(best_position, connection_type)

    def move_detectives(self, detectives, by_human=False):
        new_positions = []
        for detective in detectives:
            # Get neighbors of detective's node
            neighbors_detective, connection_types = self.get_neighbors(detective)

            # Todo: Order in which detectives can move is arbitrary => Player/AI can move them in any possible order
            #  but are not allowed to occupy one position with more than one detective

            # Check if connections to neighbors are by ferry, if so discard them
            valid_neighbors = [neighbor for index, neighbor in enumerate(neighbors_detective)
                               if connection_types[index] != "ferry" and neighbor not in new_positions]
            valid_connection_types = [connection_type for index, connection_type in enumerate(connection_types)
                                      if connection_type != "ferry" and neighbors_detective[index] not in new_positions]

            # Determine position where the detective should move
            best_position = valid_neighbors[1]
            connection_type = valid_connection_types[1]

            if by_human:
                valid_input = False
                while not valid_input:
                    player_input = input("Input position to which detective {} should move: ".format(detective.index))
                    try:
                        player_input = int(player_input)
                    except Exception:
                        print("Invalid input, not a valid position")
                    if player_input in valid_neighbors:
                        valid_input = True
                        best_position = player_input
                        input_index = valid_neighbors.index(best_position)
                        connection_type = valid_connection_types[input_index]
                        print("Valid input, Detective {} moved to position {}".format(detective.get_index(),
                                                                                      best_position))
                    else:
                        valid_input = False
                        print("Invalid input, please try again")

            # Move detective
            new_positions.append(best_position)
            detective.move(best_position, connection_type)

    def get_neighbors(self, player):
        connection_types = []
        if player.name == "Mister_X":
            network = self.mister_x_network
        else:
            network = self.detectives_network
        player_pos = player.get_position()
        try:
            simple_neighbors = list(network.neighbors(player_pos))
            # Needed, as network.neighbors only returns a list of all neighbors, disregarding the number of edges between the nodes
            neighbors = simple_neighbors.copy()
            for neighbor_index, neighbor in enumerate(simple_neighbors):
                edges = network.get_edge_data(player_pos, neighbor)
                for edge_index in range(len(edges)):
                    connection_types.append(edges[edge_index]["type"])
                    # Insert neighbor multiple times to handle multi-edges
                    if edge_index > 0:
                        neighbors.insert(neighbor_index, neighbor)
        except Exception:
            neighbors = []

        # neighbors = [neighbor for net_neighbors in network_neighbors for neighbor in net_neighbors]
        return neighbors, connection_types

    def get_valid_neighbors(self, player, detectives, neighbors, connection_types):
        valid_neighbors = neighbors
        valid_connection_types = connection_types
        if player.name == "Mister_X":
            # Check if neighbors are occupied by a detective, if so discard them
            detective_positions = [detective.get_position() for detective in detectives]
            valid_neighbors = [neighbor for neighbor in neighbors if neighbor not in detective_positions]
            valid_connection_types = [connection_types[neighbor_index] for neighbor_index, neighbor
                                      in enumerate(neighbors) if neighbor not in detective_positions]

        # Discard neighbors for which a ticket is needed that is unavailable
        for connection_index, connection_type in enumerate(valid_connection_types):
            if player.tickets[connection_type] == 0:
                valid_connection_types.remove(connection_type)
                valid_neighbors.pop(connection_index)

        return valid_neighbors, valid_connection_types

    def calculate_shortest_paths(self, mister_x, detectives, for_detectives=False):
        distances = {}
        shortest_paths = {}
        transportation_types = {}
        for detective in detectives:
            # Skip the computation for the ferry-network, if we compute the distances for the detectives,
            # as they are not able to use the ferry
            if for_detectives:
                network = self.detectives_network
                source = detective.get_position()
                target = mister_x.get_position()
            else:
                network = self.mister_x_network
                source = mister_x.get_position()
                target = detective.get_position()
            try:
                # Calculate the distance of the shortest paths
                shortest_path_length = nx.shortest_path_length(network, source, target)
                distances[detective.get_index()] = shortest_path_length

                # Calculate all shortest paths taking into account multi-edges
                shortest_paths_of_detective = list(nx.all_simple_paths(network, source, target, cutoff=shortest_path_length))
                shortest_paths_edges = [list(path) for path in map(nx.utils.pairwise, shortest_paths_of_detective)]

                # Calculate transportation types of the shortest paths
                transportation_types_of_detective = []

                for path_edges in shortest_paths_edges:
                    path_transportation_types = []
                    u = None
                    v = None
                    key = None
                    for path_edge in path_edges:
                        for network_edge in network.edges(data=True, keys=True):
                            if sorted(path_edge) == sorted((network_edge[0], network_edge[1])):
                                path_transportation_types.append(network_edge[3]["type"])
                                u = network_edge[0]
                                v = network_edge[1]
                                key = network_edge[2]
                                break

                    network.remove_edge(u, v, key)

                    transportation_types_of_detective.append(path_transportation_types)

                shortest_paths[detective.get_index()] = shortest_paths_of_detective

                transportation_types[detective.get_index()] = transportation_types_of_detective

            except nx.NodeNotFound:
                print("Either node {} or node {} not found in {}".format(detective.get_position(), mister_x.get_position(), network.name))
            except nx.NetworkXNoPath:
                print("No path between position {} and position {} in {}".format(detective.get_position(), mister_x.get_position(), network.name))

        return distances, shortest_paths, transportation_types

    def tostring(self):
        return self.pieces

    def move_player(self, move, player):
        # Todo: Implement, therefore define how move looks like
        return 0
