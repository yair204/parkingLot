import parkingLot
import ticket

def main():
    parking_lot_obj = parkingLot.AutomatedParkingLot(7,7,7) 
    parking_lot_obj.allocate_n_slots()
    ticket_obj = ticket.Ticket(1,2)
    ticket_obj.set_csv_file()
    for _ in range(8):
        print(parking_lot_obj.park_vehicle(ticket_obj,"corolla",7890,"red","S" ,"B"))
        parking_lot_obj.park_vehicle(ticket_obj,"corolla",7890,"red","M" ,"B")
        parking_lot_obj.park_vehicle(ticket_obj,"corolla",7890,"red","L" ,"B")    
    
    
    
    
    
if __name__ == "__main__":
    main()