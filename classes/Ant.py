from dataclasses import dataclass
from classes.City import City

@dataclass
class Ant:
    __current_city : City
    __path : list[City]
    __rate_phero : int
    __travel_length : float
    isCarryingFood:bool

    def get_position(self) -> City:
        return self.__current_city 

    def set_position(self, City: City) -> None:
        self.__route.append(City)
        self.__current_city = City
   
    def get_route(self) -> list[City]:
        return self.__path

    def reset_route(self) -> None:
        self.__path = []    
    
    def move(self, City: City) -> None: # choisir move ou set_position
        self.__path.append(City)

    def set_travel_length(self, length: int) -> None:
        self.__length_road = length

    def get_travel_length(self) -> int:
        return self.__length_road

    
    

