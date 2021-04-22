from player import Player


class Detective(Player):
    def __init__(self, index, start_position, num_taxi_tickets=11, num_bus_tickets=8, num_metro_tickets=4,
                 needs_tickets=True, color='red'):
        # Call init-function of abstract player to set the current and previous position
        Player.__init__(self, start_position=start_position, color=color)

        # Set number of tickets
        self.tickets = {"taxi": num_taxi_tickets, "bus": num_bus_tickets, "metro": num_metro_tickets}

        # Create ticket history which gets filled with the used tickets
        self.ticket_history = []
        self.name = "Detective"
        self.index = index

    def can_move(self, ticket_type):

        if ticket_type == "taxi":
            return self.num_taxi_tickets > 0
        elif ticket_type == "bus":
            return self.num_bus_tickets > 0
        elif ticket_type == "metro":
            return self.num_metro_tickets > 0
        else:
            print("Unknown ticket type detected when moving detective")
            return False

    def move(self, new_position, ticket_type="taxi"):

        if self.can_move(ticket_type):

            Player.set_new_position(self, new_position)

            if self.needs_tickets:
                # Reduce number of tickets
                if ticket_type == "taxi":
                    self.num_taxi_tickets -= 1
                elif ticket_type == "bus":
                    self.num_bus_tickets -= 1
                elif ticket_type == "metro":
                    self.num_metro_tickets -= 1
        else:
            self.set_static()

    def get_status(self):
        status = "Status detective: \n" \
                 "Detective index: {} \n" \
                 "Detective color: {} \n" \
                 "Current position: {} \n" \
                 "Previous positions: {} \n" \
                 "Number of taxi tickets: {} \n" \
                 "Number of bus tickets: {} \n" \
                 "Number of metro tickets: {} \n".format(self.index, self.color, self.position, self.prev_positions,
                                                         self.num_taxi_tickets,
                                                         self.num_bus_tickets, self.num_metro_tickets)
        return status

    def set_static(self):
        print("Detective {} cannot move because he has not got the required tickets".format(self.get_index()))

    def get_index(self):
        return self.index

    def get_tickets(self):
        return [self.num_taxi_tickets, self.num_bus_tickets, self.num_metro_tickets]
