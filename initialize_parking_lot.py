import parkingLot
def initialize_parking_slot( number_bikes: int, number_cars: int,number_buses: int) -> parkingLot.AutomatedParkingLot:
    """
    initialize object of parking slot

    Args:
        number_bikes (int): number of bikes slot
        number_cars (int): number of cars slot
        number_buses (int): number of buses slot

    Returns:
        parkingLot.AutomatedParkingLot: object of AutomatedParkingLot
    """
    parking_lot_obj = parkingLot.AutomatedParkingLot(number_bikes,number_cars,number_buses) 
    parking_lot_obj.allocate_n_slots()
    return parking_lot_obj