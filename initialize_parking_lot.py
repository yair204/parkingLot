import parkingLot
import logger_parking_lot as lg
def initialize_parking_lot(number_bikes: str, number_cars: str,number_buses: str)-> parkingLot.AutomatedParkingLot:
    """
    initialize object of parking lot

    Args:
        number_bikes (int): number of bikes slot
        number_cars (int): number of cars slot
        number_buses (int): number of buses slot

    Returns:
        parkingLot.AutomatedParkingLot: object of AutomatedParkingLot
    """
    lg.logger.debug("initialize object of parking lot")
    lg.logger.debug("main window is opened")
    parking_lot_obj = parkingLot.AutomatedParkingLot(number_bikes,number_cars,number_buses) 
    parking_lot_obj.allocate_n_slots()
    return parking_lot_obj