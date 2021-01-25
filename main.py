from game import Game

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
game.play_game()
