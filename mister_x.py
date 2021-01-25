from player import Player


class MisterX(Player):
    # Todo: Set correct number of tickets
    def __init__(self, start_position=10, num_taxi_tickets=10, num_bus_tickets=10, num_metro_tickets=10,
                 num_black_tickets=5, color='grey'):
        # Call init-function of abstract player to set the current and previous position
        Player.__init__(self, start_position=start_position, color=color)

        # Set number of tickets
        self.tickets = {"taxi": num_taxi_tickets, "bus": num_bus_tickets, "metro": num_metro_tickets, "ferry": num_black_tickets}

        # Create ticket history which gets filled with the used tickets
        self.ticket_history = []
        self.name = "Mister_X"

    def move(self, new_position, ticket_type="taxi"):
        Player.set_new_position(self, new_position)

        # Append used ticket to ticket history
        self.ticket_history.append(ticket_type)

        # Reduce number of tickets
        self.tickets[ticket_type] -= 1

        # Todo: Add case where player/central intelligence decides to use a black ticket for something else than a ferry

    def get_status(self):
        status = "Status Mister X: \n" \
                 "Color: {} \n" \
                 "Current position: {} \n" \
                 "Previous positions: {} \n" \
                 "Number of taxi tickets: {} \n" \
                 "Number of bus tickets: {} \n" \
                 "Number of metro tickets: {} \n"\
                 "Number of black tickets: {} \n".format(self.color, self.position, self.prev_positions, self.tickets["taxi"],
                                                         self.tickets["bus"], self.tickets["metro"],
                                                         self.tickets["ferry"])
        return status

    def get_ticket_history(self):
        return self.ticket_history
