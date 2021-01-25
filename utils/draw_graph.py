import networkx as nx
import matplotlib.pyplot as plt


def draw_network(network, node_color=None, node_labels=None, single_network=True):
    positions = {node: network.nodes._nodes[node]["position"] for node in network.nodes}
    edge_colors = [edge_attribute["color"] for _, _, edge_attribute in network.edges(data=True)]
    edge_widths = [edge_attribute["width"] for _, _, edge_attribute in network.edges(data=True)]
    # Todo: Find better way to show duplicate/parallel edges, then remove dotted-style
    nx.draw(network, with_labels=True, node_color=node_color, pos=positions, edge_color=edge_colors, width=edge_widths, style="dotted")
    #offset_pos = {key: [pos - 0.035 * (network_index + 1) if index == 1 else pos for index, pos in enumerate(value)] for (key, value) in positions.items()}
    #nx.draw_networkx_labels(network, labels=node_labels, pos=offset_pos, font_size=10)
    plt.pause(0.001)
    if single_network:
        plt.show()


def draw_graph_and_players(network, mister_x, detectives, positions=None, by_human=False):

    node_colors = []
    node_labels = {}
    for node_index in list(network):
        # Base color of nodes is blue (= #1f78b4)
        node_colors.append('#1f78b4')
        if node_index == mister_x.get_position():
            # If Mister X stands on the current position mark it with the corresponding color
            node_colors[-1] = mister_x.color
        else:
            # Else iterate over detectives to see whether one of them stands on the current position
            for detective in detectives:
                if node_index == detective.get_position():
                    # If a detective stands on the current position mark it red
                    node_colors[-1] = detective.color

        node_labels[node_index] = " Neighbors: " + str(list(dict(network.adj[node_index]).keys()))
    draw_network(network, node_color=node_colors, node_labels=node_labels, single_network=False)
    # if by_human:
    if True:
        plt.ion()
    plt.show()
