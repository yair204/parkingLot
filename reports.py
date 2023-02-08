
import parkingLot
import ticket
import datetime
import csv
import fee_calculator

def track_of_capacity(AutomatedParkingLot: object)->list:
    """_summary_

    Args:
        AutomatedParkingLot (object): 

    Returns:
        list: The amount of free parking, and the amount of occupancy
    """
    slots_full =[ticket.slot_ID for ticket in AutomatedParkingLot.tickets_list]
    slots_full.sort()
    current_time = datetime.datetime.now()
    return [f"in the {current_time} tis slot fully: {slots_full}"]

def specific_company(AutomatedParkingLot: object, company: str)->list:
    """_summary_

    Args:
        AutomatedParkingLot (object): 

    Returns:
        list: The amount of free parking, and the amount of occupancy
    """
    slots_full =[ticket.plate_num for ticket in AutomatedParkingLot.tickets_list if ticket.compony_vehicle == company]
  
    return [f"plate number of all the vehicles they are -{company}- : {slots_full}"]

def specific_color(AutomatedParkingLot: object, color: str)->list:
    """_summary_

    Args:
        AutomatedParkingLot (object): 

    Returns:
        list: The amount of free parking, and the amount of occupancy
    """
    slots_full =[ticket.plate_num for ticket in AutomatedParkingLot.tickets_list if ticket.color_vehicle == color]
  
    return [f"plate number of all the vehicles they are -{color}- : {slots_full}"]

def specific_type(AutomatedParkingLot: object, type: str)->list:
    """_summary_

    Args:
        AutomatedParkingLot (object): 

    Returns:
        list: The amount of free parking, and the amount of occupancy
    """
    slots_full =[ticket.plate_num for ticket in AutomatedParkingLot.tickets_list if ticket.type_vehicle == type]
  
    return [f"plate number of all the vehicles they are -{type}- : {slots_full}"]

def specific_slot_ID(AutomatedParkingLot: object, plate_num: int)->str:
    """Search slot by given plate number

    Args:
        AutomatedParkingLot :object of parking lot 
        plate_num:int

    Returns:
        str: The slot id in format string
    """
    slot_ID = (ticket.slot_ID for ticket in AutomatedParkingLot.tickets_list if ticket.plate_num == plate_num)
    return f"vehicle number: {plate_num} \n parking in slot number : {slot_ID}"  

def vehicle_parked_in_period_time(fileName:str) -> int:
    
    csv_list = list(csv.reader(open(fileName, 'r')))
    pay = csv_list[0].index('payment')
    return sum(int(col) for row in csv_list[1:] for col in row[pay:])
   
def parked_more_24_hours(AutomatedParkingLot: object) -> list[int]:
    return [ticket.plate_num for ticket in AutomatedParkingLot.tickets_list if fee_calculator.calculate_time(ticket)> 24]    
    
print(vehicle_parked_in_period_time('data.csv'))
