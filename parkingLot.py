import parking_slot
import vehicle


class AutomatedParkingLot:
    """
        Class AutomatedParkingLot generate parking lot
            with 3 type of slots SP, MP, LP
        Attr
    
    """
    def __init__(self,S_slots:int,M_slots:int,L_slots:int) -> None:
        self.S_slots = S_slots
        self.M_slots = M_slots
        self.L_slots = L_slots
        self.gate_A = "A"
        self.gate_B = "B"
        self.gate_C = "C"
        self.slots_SP_list = [] 
        self.slots_MP_list = []
        self.slots_LP_list = []
        
        self.vehicle_dict = {}
        
        
    def allocate_n_slots(self):
        for slot in range(self.S_slots): 
            slot_ = parking_slot.ParkingSlot("SP" ,f"S{slot}",True)
            self.slots_SP_list.append(slot_)

        for slot in range(self.M_slots): 
            slot_ = parking_slot.ParkingSlot("MP" ,f"M{slot}",True) 
            self.slots_MP_list.append(slot_)

        for slot in range(self.L_slots): 
            slot_ = parking_slot.ParkingSlot("LP" ,f"L{slot}",True) 
            self.slots_LP_list.append(slot_)
            
    
    def park_vehicle(self,compony, plate_num, color,car_type,gate):
        
        if car_type == "S":  
            self.vehicle_dict[self.allocate_nearly_slot(gate,self.slots_SP_list)] = vehicle.Bike(compony, plate_num, color, car_type)
            # return ticket_obj.add_to_csvFile(self.allocate_nearly_slot(gate,self.slots_SP_list),car_type,compony,plate_num,color,time.strftime("%Y%m%d"),time.strftime("%H%M"),0)
        
        if car_type == "M":
            self.vehicle_dict[self.allocate_nearly_slot(gate,self.slots_MP_list)] = vehicle.Car(compony, plate_num, color,car_type)
            # return ticket_obj.add_to_csvFile(self.allocate_nearly_slot(gate,self.slots_MP_list),car_type,compony,plate_num,color,time.strftime("%Y%m%d"),time.strftime("%H%M"),0)
               
        if car_type == "L": 
            self.vehicle_dict[self.allocate_nearly_slot(gate,self.slots_LP_list)] = vehicle.Bus(compony, plate_num, color,car_type)
            # return ticket_obj.add_to_csvFile(self.allocate_nearly_slot(gate,self.slots_LP_list),car_type,compony,plate_num,color,time.strftime("%Y%m%d"),time.strftime("%H%M"),0)
        
    def unpark_vehicle(self):
        pass
    
    def allocate_nearly_slot(self,gate:str,slots_list:list):
        
        if gate == self.gate_A:
            for i in slots_list:
                if i.is_empty:
                    i.is_empty = False
                    return i.ID
            print("Sorry!\nThe parking lot is full!")
            return -1
            
        
        if gate == self.gate_B:
            for i in range(len(slots_list)//2+1):
                if slots_list[len(slots_list)//2-i].is_empty:
                    slots_list[len(slots_list)//2-i].is_empty = False
                    return slots_list[len(slots_list)//2-i].ID
                elif slots_list[len(slots_list)//2+i].is_empty:
                    slots_list[len(slots_list)//2+i].is_empty = False
                    return slots_list[len(slots_list)//2+i].ID
                
            print("Sorry!\nThe parking lot is full!")
            return -1
        
        
        if gate == self.gate_C:       
            for i in slots_list[::-1]:
                if i.is_empty:
                    i.is_empty = False
                    return i.ID
            print("Sorry!\nThe parking lot is full!")
            raise -1
        
       
    def add_gate(self, new_gate:str):
        assert new_gate == str 
        self.gate_D = new_gate
        


# a = AutomatedParkingLot(7,7,7)
# a.allocate_n_slots()
# b = []
# b.extend(i.ID for i in a.slots_LP_list)
# print(b)
