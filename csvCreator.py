import csv

 
def set_csv_file(fileName, *list_):
    
    headers = ["slot_ID","type_car","company","plat_number","color","date","entry time","exit time"]
    with open(f"{fileName}.csv", 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerow(list_)  
    
    
    