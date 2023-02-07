import parkingLot
import ticket

def main():
    parking_lot_obj = parkingLot.AutomatedParkingLot(7,7,7) 
    parking_lot_obj.allocate_n_slots()
    # ticket_obj = ticket.Ticket(1,2)
    # ticket_obj.set_csv_file()
    for _ in range(4):
        parking_lot_obj.park_vehicle("corolla",7890,"red","S" ,"B")
        parking_lot_obj.park_vehicle("corolla",7890,"red","M" ,"B")
        parking_lot_obj.park_vehicle("corolla",7890,"red","L" ,"B")  
         
    parking_lot_obj.park_vehicle("corolla",900,"red","S" ,"A")

    for i in parking_lot_obj.slots_SP_list:
        print(i.type,i.ID,i.is_empty)
   
    parking_lot_obj.remove_vehicle(900)
    
    print("\nafter removing\n")
    for i in parking_lot_obj.tickets_list:
        print(i.entry_time)
    
    
    
    
if __name__ == "__main__":
    main()