class Edge:
    """
    This class represents the undirected edges which connect the different nodes.
    """

    def __init__(self, start_node, end_node, is_taxi_line=False, is_bus_line=False, is_metro_line=False, is_ferry_line=False):
        """
        Init-function of the Edge-class.
        :param start_node: First node which is connected to the edge
        :param end_node: Second node which is connected to the edge
        :param is_taxi_line: Boolean flag which shows if the current edge is a line of the taxi network
        :param is_bus_line: Boolean flag which shows if the current edge is a line of the bus network
        :param is_metro_line: Boolean flag which shows if the current edge is a line of the metro network
        :param is_ferry_line: Boolean flag which shows if the current edge is a line of the ferry network
        """

        self.start_node = start_node
        self.end_node = end_node
        self.is_taxi_line = is_taxi_line
        self.is_bus_line = is_bus_line
        self.is_metro_line = is_metro_line
        self.is_ferry_line = is_ferry_line
