#5. Write a class Train which has methods to book a ticket, get status (no. of seats), and get fare information of train running under Indian Railways.

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"Train: {self.name}")
        print(f"Available Seats: {self.seats}")

    def fareInfo(self):
        print(f"The fare for {self.name} is Rs {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print("Ticket booked!")
            self.seats -= 1
        else:
            print("Sorry, no seats available!")


# Example usage
t = Train("Rajdhani Express", 1500, 2)
t.getStatus()
t.bookTicket()
t.getStatus()
t.fareInfo()
