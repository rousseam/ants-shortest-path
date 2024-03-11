from dataclasses import dataclass
from classes.City import City

@dataclass
class Ant:
    __current_city : City
    __route : list[City]
    __rate_phero : int
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
