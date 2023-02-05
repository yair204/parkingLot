import time
import math


class Ticket:
    def __init__(self, time, date) -> None:
        self.time = time
        self.date = date

    def get_time(self):
        return self.time

    def get_date(self):
        return self.date


a = Ticket("22:51", "20230204")


def calculate_time(Ticket: object) -> int:
    """Calculates the time the car was parked in the parking lot

    Args:
        Ticket (object): Ticket class object

    Returns:
        total_time:(int) final time the vehicle was in the parking lot, rounded up.
    """
    entrance_time = Ticket.get_time()  # entry time
    current_time = time.strftime("%H%M")  # departure time
    current_date = time.strftime("%Y%m%d")  # today's date.
    days = int(current_date[6:]) - int(Ticket.get_date()[6:])
    minutes = (60 - int(entrance_time[3:])) + int(current_time[3:])
    if days == 0:
        hours = ((int(current_time[:2])) - (int(entrance_time[:2]))) * 60
        return math.ceil(((hours + minutes) / 60))  # total time rounded up.
    elif days > 0:
        hours = (int(current_time[:2]) + (24 - int(entrance_time[:2]))) * 60
        if days == 1:
            return math.ceil(((hours + minutes) / 60))  # total time rounded up.
        else:
            return (
                math.ceil(((hours + minutes) / 60)) + 24 * days - 1
            )  # total time rounded up.


def calculate_price(Ticket: object) -> int:
    """Calculates the price of parking according to the hours and type of vehicle

    Args:
        Ticket (object): Ticket class object
    Returns:
        int: The final price required
    """
    hours = calculate_time(a)
    if hours > 24:
        print("+100")
    if hours > 3:
        if a.type_vic == "L":
            print("L")
        elif a.type_vic == "M":
            print("M")
        else:
            print("S")
    return 20 * hours
