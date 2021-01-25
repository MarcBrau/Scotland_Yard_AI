class Node:
    """
    This class represents the nodes of the different networks on the map.
    """
    def __init__(self, index, edges=None, is_taxi_stop=False, is_bus_stop=False, is_metro_stop=False,
                 is_ferry_stop=False):
        """
        Init-function of the Node-class.
        :param index: Unique integer index of the node
        :param edges: List of edges that connect this node to other nodes
        :param is_taxi_stop: Boolean flag which shows if the current node is a node of the taxi network
        :param is_bus_stop: Boolean flag which shows if the current node is a node of the bus network
        :param is_metro_stop: Boolean flag which shows if the current node is a node of the metro network
        :param is_ferry_stop: Boolean flag which shows if the current node is a node of the ferry network
        """
        self.index = index

        if edges is None:
            edges = []
            self.neighbors_index = []
        else:
            self.neighbors_index = [edge.start_node.index if edge.start_node.index != self.index
                                    else edge.end_node.index for edge in edges]
        self.edges = edges
        self.is_taxi_stop = is_taxi_stop
        self.is_bus_stop = is_bus_stop
        self.is_metro_stop = is_metro_stop
        self.is_ferry_stop = is_ferry_stop

    def add_edges(self, edges):
        self.edges.append(edges)
        new_neighbor_indexes = [edge.start_node.index if edge.end_node.index == self.index else edge.end_node.index
                                for edge in edges]
        new_neighbor_indexes = list(filter(lambda x: x == self.neighbors_index, new_neighbor_indexes))
        self.neighbors_index.append(new_neighbor_indexes)

    def get_edges(self):
        return self.edges

    def get_index(self):
        return self.index
