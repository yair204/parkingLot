
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
        
        
        self.filename = "data.csv"

    def get_time(self):
        return self.entry_time

    def get_date(self):
        return self.entry_time.date()
    
    def get_plate_num(self):
        return self.plate_num

    def set_csv_file(self):
        
        headers = ["slot_ID","type_car","compony","plat_number","color","date","entry time","exit time"]
        with open(self.filename, 'w', newline='') as csv_file:
            self.writer = csv.writer(csv_file)
            self.writer.writerow(headers)
           
    def add_to_csvFile(self,*list_):
        with open(self.filename, 'a+', newline='') as csv_file:
            self.writer = csv.writer(csv_file)
            self.writer.writerow(list_)  
        return list_
        
        
      
            
           

# t = Ticket(1,1)
# t.set_csv_file()