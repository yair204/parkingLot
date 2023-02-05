import csv

class Ticket:
    def __init__(self, time, date) -> None:
        self.time = time
        self.date = date
        self.filename = "data.csv"

    def get_time(self):
        return self.time

    def get_date(self):
        return self.date

    def set_csv_file(self):
        
        headers = ["slot_ID","type_car","compony","plat_number","color","date","entry time","exit time"]
        with open(self.filename, 'w', newline='') as csv_file:
            self.writer = csv.writer(csv_file)
            self.writer.writerow(headers)

            
                 
    def add_to_csvFile(self,*list_):
        with open(self.filename, 'a+', newline='') as csv_file:
            self.writer = csv.writer(csv_file)
            self.writer.writerow(list_)      
        
        
      
            
           

t = Ticket(1,1)
t.set_csv_file()