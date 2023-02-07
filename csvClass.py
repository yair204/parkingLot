import csv

class Csv:
    def __init__(self) -> None:
         self.filename = "data.csv"
         
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
        
        