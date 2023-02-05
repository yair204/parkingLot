

class Vehicle:
    def __init__(self,compony:str,plate_num:int,color:str) -> None:
        self.compony = compony
        self.plate_num = plate_num
        self.color = color
       
    def get_car_compony(self):
        return self.compony
    
    def get_plate_num(self):
        return self.plate_num
   
    def get_color(self):
        return self.color
   
    
    
class Car(Vehicle):
    def __init__(self, compony: str, plate_num: int, color: str,type:str) -> None:
        super().__init__(compony, plate_num, color)
        self.type = type
     
    def get_car_type(self):
        return self.type
        

class Bus(Vehicle):
    def __init__(self, compony: str, plate_num: int, color: str,type:str) -> None:
        super().__init__(compony, plate_num, color)
        self.type = type
    
    def get_car_type(self):
        return self.type
               
        
class Bike(Vehicle):
    def __init__(self, compony: str, plate_num: int, color: str,type:str) -> None:
        super().__init__(compony, plate_num, color)
        self.type = type  
     
    def get_car_type(self):
        return self.type
        
              
        
# a = Car("corolla" , 1234567,"white","A")

# print(a.get_car_compony())
# print(a.get_plate_num())
# print(a.get_car_type())