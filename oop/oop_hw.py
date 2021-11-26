#qs1 the rectangle class
class Rectangle:
    def __init__(self,len,width):
        self.__len = len
        self.__width = width
        
    def area(self):
        return self.__len*self.__width
    
#qs2 the vehicle class

class Vehicle:
    def __init__(self,maxSpeed,meliage):
        self.__maxSpeed = maxSpeed
        self.meliage = meliage
        
#qs3 empty vehicle class

class Vehicle_:
    pass

#qs4 child class Bus

class Bus(Vehicle):
    pass


        
        