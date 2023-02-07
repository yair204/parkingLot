from datetime import datetime
import time
import math


class Ticket:
    def __init__(self,slot_ID ,vehicle_obj:object ) -> None:
        self.slot_ID = slot_ID
        self.vehicle_obj = vehicle_obj
        self.type_vehicle = vehicle_obj.type
        self.plate_num = vehicle_obj.plate_num
        self.compony_vehicle = vehicle_obj.compony
        self.color_vehicle = vehicle_obj.color
       
        self.entry_time = datetime.now()

    def get_time(self):
        return self.entry_time

    def get_date(self):
        return self.entry_time.date()
    
    def get_plate_num(self):
        return self.plate_num

    
        
        
      
            
           

# t = Ticket(1,1)
# t.set_csv_file()