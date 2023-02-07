from datetime import datetime
import time
import math


def calculate_time(ticket_obj: object) -> int:
    """Calculates the time the car was parked in the parking lot

    Args:
        Ticket (object): Ticket class object

    Returns:
        total_time:(int) final time the vehicle was in the parking lot, rounded up.
    """
    enter_time = ticket_obj.get_time()
    exit_time = datetime.now()
    different_time = exit_time - enter_time
    total_seconds = different_time.total_seconds()
    hours = total_seconds / 3600
    return math.ceil(hours)  # total time round up


def calculate_price(ticket_obj: object, price_of_days=480) -> int:
    """Calculates the price of parking according to the hours and type of vehicle

    Args:
        Ticket (object): Ticket class object
    Returns:
        int: The final price required
    """
    hours = calculate_time(ticket_obj)
    
    total = 0
    exceeding_rate = 0
    if hours > 24:  # Extra charge over 24 hours
        days, hours = divmod(hours, 24)
        total = days * price_of_days + 100 * days
    if hours > 3:  # Extra charge over 3 hours
        exceeding_rate = hours - 3
        if ticket_obj.type_vehicle == "L":
            total += exceeding_rate * 40
        elif ticket_obj.type_vehicle == "M":
            total += exceeding_rate * 30
    return total + (hours - exceeding_rate) * 20  # total price


