import parkingLot
import ticket

def main():
    parkinglot_obj = parkingLot.AutomatedParkingLot(21) 
    parkinglot_obj.allocate_n_slots()
    ticket_obj = ticket.Ticket(1,2)
    ticket_obj.set_csv_file()
    # ticket_obj.add_to_csvFile([1,2,3,4,5,2,3,4])
    parkinglot_obj.park_vehicle(ticket_obj,"corolla",123456,"red","S")
    
    
    
    
    
    
if __name__ == "__main__":
    main()