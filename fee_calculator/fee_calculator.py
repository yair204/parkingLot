from datetime import datetime
import time
import math


class Ticket:
    def __init__(self,type_vic, ) -> None:
        self.time_ = datetime.now()
        self.type_vic = type_vic
        self.if_up_day = False
    def get_time(self):
        return self.time_.time()

    def get_date(self):
        return self.time_.date()

time_ = datetime.now()
a = Ticket(time_, "M")


def calculate_time(Ticket: object) -> int:
    """Calculates the time the car was parked in the parking lot

    Args:
        Ticket (object): Ticket class object

    Returns:
        total_time:(int) final time the vehicle was in the parking lot, rounded up.
    """
    enter_time = Ticket.get_time()
    exit_time = datetime.now()
    different_time = exit_time - enter_time
    total_seconds = different_time.total_seconds()
    hours = total_seconds / 3600
    return math.ceil(hours)  # total time round up


def calculate_price(Ticket: object, price_of_days=480) -> int:
    """Calculates the price of parking according to the hours and type of vehicle

    Args:
        Ticket (object): Ticket class object
    Returns:
        int: The final price required
    """
    hours = calculate_time(a)
    print(hours)
    total = 0
    exceeding_rate = 0
    if hours > 24:  # Extra charge over 24 hours
        Ticket.if_up_day = True
        days, hours = divmod(hours, 24)
        total = days * price_of_days + 100 * days
    if hours > 3:  # Extra charge over 3 hours
        exceeding_rate = hours - 3
        if a.type_vic == "L":
            total += exceeding_rate * 40
        elif a.type_vic == "M":
            total += exceeding_rate * 30
    return total + (hours - exceeding_rate) * 20  # total price


calculate_price(a)
