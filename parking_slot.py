
class ParkingSlot:
    def __init__(self,type:str,ID:int,is_empty:bool) -> None:
        self.type = type
        self.color = ''
        self.ID = ID
        self.is_empty = is_empty
        
    def get_vehicle(self):
        print("The vehicle added successfully!")
    
    def remove_vehicle(self):
        print("The vehicle successfully removed!")
    