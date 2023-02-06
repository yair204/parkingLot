

class Vehicle:
    """Defined abstract vehicle class

        Attribute:

            compony:str
                car compony
            
            plate_num:int
                car's plate number
                
            color:str
                car's color

        Methods:
            get_car_compony:
            get_plate_num:
            get_color:
           
        Return:
            vehicle

    """

   
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
    """
        Class Car inheritor from Vehicle class

    Args:
        Vehicle (_type_): str
            type of car
            
    Methods:
        get_vehicle_attributes()
    """
    def __init__(self, compony: str, plate_num: int, color: str,type:str) -> None:
        super().__init__(compony, plate_num, color)
        self.type = type
     
    def get_vehicle_attributes(self):
        return self.type,self.color,self.plate_num,self.compony
        

class Bus(Vehicle):
    """
        Class Bus inheritor from Vehicle class

    Args:
        Vehicle (_type_): str
            type of bus
            
    Methods:
        get_vehicle_attributes()
    """
    def __init__(self, compony: str, plate_num: int, color: str,type:str) -> None:
        super().__init__(compony, plate_num, color)
        self.type = type
    
    def get_vehicle_attributes(self):
        return self.type,self.color,self.plate_num,self.compony
               
        
class Bike(Vehicle):
    """
        Class bike inheritor from Vehicle class

    Args:
        Vehicle (_type_): str
            type of bike
            
    Methods:
        get_vehicle_attributes()
    """
    def __init__(self, compony: str, plate_num: int, color: str,type:str) -> None:
        super().__init__(compony, plate_num, color)
        self.type = type  
     
    def get_vehicle_attributes(self):
        return self.type,self.color,self.plate_num,self.compony
        
              
        
# a = Car("corolla" , 1234567,"white","A")

# print(a.get_car_compony())
# print(a.get_plate_num())
# print(a.get_car_type())