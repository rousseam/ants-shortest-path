from dataclasses import dataclass
from classes.City import City

@dataclass
class Ant:
    __current_city : City
    __route : list[City]
    __rate_phero : int
    __length_road : float
    isCarryingFood:bool

    def get_position(self):
        return self.__current_city 
    def set_position(self,City):
        self.__route.append(City)
        self.__current_city = City
   
    def get_route(self):
        return self.__route
    def reset_route(self):
        self.__route=[]    
    
    def move(self, City):
        self.__route.append(City)
    def set_length_road(self,L):
        self.__length_road=L
    def get_length_road(self):
        return self.__length_road

    
    

