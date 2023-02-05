import parking_slot
import vehicle
import ticket
import time

class AutomatedParkingLot:
    def __init__(self,capacity:int) -> None:
        self.capacity = capacity
        self.gate_A = "A"
        self.gate_B = "B"
        self.gate_C = "C"
        self.slots_SP_list = [] 
        self.slots_MP_list = []
        self.slots_LP_list = []
        
        

    def allocate_n_slots(self):
        for slot in range(self.capacity//3): 
            slot_ = parking_slot.ParkingSlot("SP" ,slot,True)
            self.slots_SP_list.append(slot_)

        for slot in range(self.capacity//3,(self.capacity*2)//3): 
            slot_ = parking_slot.ParkingSlot("MP" ,slot,True) 
            self.slots_MP_list.append(slot_)

        for slot in range((self.capacity*2)//3,self.capacity): 
            slot_ = parking_slot.ParkingSlot("LP" ,slot,True) 
            self.slots_LP_list.append(slot_)
            
    
    def park_vehicle(self,ticket_obj,compony, plate_num, color,car_type):
        
        if car_type == "S": 
            s = 0
            if self.slots_SP_list[s].is_empty:
                vehicle.Bike(compony, plate_num, color,car_type)
                ticket_obj.add_to_csvFile(self.slots_SP_list[s].ID,car_type,compony,plate_num,color,time.strftime("%Y%m%d"),time.strftime("%H%M"),0)
                s +=1
        if car_type == "M": 
            vehicle.Car(compony, plate_num, color,car_type)
            m = 0
            ticket_obj.add_to_csvFile(self.slots_SP_list[m].ID,car_type,compony,plate_num,color,time.strftime("%Y%m%d"),time.strftime("%H%M"),0)
            m += 1
        if car_type == "L": 
            vehicle.Bus(compony, plate_num, color,car_type) 
            l = 0
            ticket_obj.add_to_csvFile(self.slots_SP_list[l].ID,car_type,compony,plate_num,color,time.strftime("%Y%m%d"),time.strftime("%H%M"),0)
            l += 1
        
    def unpark_vehicle(self):
        pass
        
        
    def add_gate(self, new_gate:str):
        assert new_gate == str 
        self.gate_D = new_gate
        


a = AutomatedParkingLot(21)
a.allocate_n_slots()
for i in a.slots_LP_list:
    print(i.ID)
    
print(a.slots_SP_list[0].ID)

