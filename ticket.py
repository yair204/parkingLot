from datetime import datetime
import time
import math


class Ticket:
    def __init__(self,slot_ID ,vehicle_obj:object ) -> None:
        
        self.slot_ID = slot_ID
        self.vehicle_obj = vehicle_obj
        self.type_vehicle = vehicle_obj.type
        self.plate_num = vehicle_obj.plate_num
        self.company_vehicle = vehicle_obj.company
        self.color_vehicle = vehicle_obj.color
        
        self.payment = 0
        self.is_up_day = False
        self.entry_time = datetime.now()
        self.exit_time = 0

    def get_time(self):
        return self.entry_time

    def get_date(self):
        return self.entry_time.date()
    
    def get_plate_num(self):
        return self.plate_num
    
    def return_ticket(self):
        return  self.slot_ID , self.type_vehicle , self.plate_num ,self.company_vehicle ,self.color_vehicle ,self.entry_time

    def set_payment(self,payment):
        self.payment = payment
        

    
        
        
      
            
           

# t = Ticket(1,1)
# t.set_csv_file()