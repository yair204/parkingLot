import parking_slot
import vehicle
import ticket
from datetime import datetime
import time
import fee_calculator
import csv

class AutomatedParkingLot:
    """
        Class AutomatedParkingLot generate parking lot
            with 3 type of slots SP, MP, LP
        
        Attributes:
            S_slots: sum of slots for type S
            M_slots: sum of slots for type M
            L_slots: sum of slots for type L
            
            gate_A:
            gate_B:
            gate_C:
             
            slots_SP_list:type list 
            slots_MP_list:type list
            slots_LP_list:type list
            
            ticker_list:list of all tickets instances
        
        Methods:
            allocate_n_slots() : create lists of al  slots with his ID and type
            park_vehicle() : create an instance of vehicle , assign slot and send it to ticket class 
            remove_vehicle() : remove any vehicle with a specific plate number, re_allocate the slot and 
                              return it's ID ,finally calculate the price
            allocate_nearly_slot() : find the nearly slot by consider the gate 
    
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
        
        self.tickets_list = []
        self.left_tickets_list = []
        
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
            
    def park_vehicle(self,company:str, plate_num:int, color:str,car_type:str,gate:str):
        
        if car_type == "S":  
            current_slot = self.allocate_nearly_slot(gate,self.slots_SP_list)
            self.tickets_list.append(ticket.Ticket(current_slot,vehicle.Bike(company, plate_num, color, car_type)))
           
    
            headers = ["slot_ID","type_car","company","plat_number","color","date","entry time","exit time","payment"]
            with open("data.csv", 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(headers)
                writer.writerow([current_slot,car_type,company,plate_num,color,datetime.now(),time.strftime(str("%H:%M:%S:")),0,20])  
            
            for _ in range(5):
                with open("data.csv", 'a+', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    
                    writer.writerow([current_slot,car_type,company,plate_num,color,datetime.now(),time.strftime(str("%H:%M:%S:")),0,20])  
                
                
            return current_slot 
            
        
        if car_type == "M":
            current_slot = self.allocate_nearly_slot(gate,self.slots_MP_list)
            self.tickets_list.append(ticket.Ticket(current_slot,vehicle.Car(company, plate_num, color, car_type)))
            return current_slot 
            
               
        if car_type == "L": 
            current_slot = self.allocate_nearly_slot(gate,self.slots_LP_list)
            self.tickets_list.append(ticket.Ticket(current_slot,vehicle.Bus(company, plate_num, color, car_type)))
            return current_slot 
    
    def remove_vehicle(self,plate_num:int):
        
        for ticket in self.tickets_list:
            if plate_num == ticket.get_plate_num():
                
                if ticket.type_vehicle == "M":
                    for m in self.slots_MP_list:
                        if m.ID == ticket.slot_ID:
                            m.is_empty = True 

                elif ticket.type_vehicle == "S":
                    for s in self.slots_SP_list:
                        if s.ID == ticket.slot_ID:
                            s.is_empty = True

                else:
                    for l in self.slots_LP_list:
                        if l.ID == ticket.slot_ID:
                            l.is_empty = True
                for item in self.left_tickets_list:
                    if (
                        plate_num == item.get_plate_num()
                        and fee_calculator.calculate_time(item) < 2
                    ):
                        self.tickets_list.remove(ticket) # remove the ticket from the list
                        return payment,ticket.slot_ID # return the payment and slot id
                payment = fee_calculator.calculate_price(ticket) # Calculate the final price
                ticket.set_payment(payment) # send the payment to ticket class
                self.left_tickets_list.append(ticket) # add the ticket to list of tickets that left
                self.tickets_list.remove(ticket) # remove the ticket from the list
                return payment,ticket.slot_ID # return the payment and slot id

        return None , None #If the plate number not exist             
    
    def allocate_nearly_slot(self,gate:str,slots_list:list):
        
        if gate == self.gate_A: # Gate A search the nearest slot by loop the list in ascending order  
            for i in slots_list:
                if i.is_empty:
                    i.is_empty = False
                    return i.ID
            print("Sorry!\nThe parking lot is full!")
            return None
            
        
        if gate == self.gate_B:# Gate B search the nearest slot by loop the list in zigzag order  
            for i in range(len(slots_list)//2+1):
                if slots_list[len(slots_list)//2-i].is_empty:
                    slots_list[len(slots_list)//2-i].is_empty = False
                    return slots_list[len(slots_list)//2-i].ID
                elif slots_list[len(slots_list)//2+i].is_empty:
                    slots_list[len(slots_list)//2+i].is_empty = False
                    return slots_list[len(slots_list)//2+i].ID
                
            print("Sorry!\nThe parking lot is full!")
            return None
        
        
        if gate == self.gate_C: # Gate C search the nearest slot by loop the list in descending order     
            for i in slots_list[::-1]:
                if i.is_empty:
                    i.is_empty = False
                    return i.ID
            print("Sorry!\nThe parking lot is full!")
            return None
               
    def add_gate(self, new_gate:str):
        assert new_gate == str 
        self.gate_D = new_gate
        


# a = AutomatedParkingLot(7,7,7)
# a.allocate_n_slots()
# b = []
# b.extend(i.ID for i in a.slots_LP_list)
# print(b)

