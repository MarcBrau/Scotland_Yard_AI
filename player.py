class Player:
    """
    This class represents an abstract player of the game.
    """
    def __init__(self, start_position, color):
        self.position = start_position
        self.color = color
        self.prev_positions = []

    def set_new_position(self, new_position):
        # Append current position to list of previous positions
        self.prev_positions.append(self.position)
        # Change current position to the new position
        self.position = new_position

    def get_position(self):
        return self.position

    def get_prev_positions(self):
        return self.prev_positions
