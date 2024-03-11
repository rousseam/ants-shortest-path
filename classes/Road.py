from dataclasses import dataclass
from City import City

@dataclass
class Road:
    __pheromone_quantity: float
    __length: float =0
    __starting_city: City
    __ending_city : City

    def set_length(self): 
        self.__length = ((self.__starting_city.x_coordinate()-self.__ending_city.x_coordinate())**2 - (self.__starting_city.y_coordinate()-self.__ending_city.y_coordinate())**2)**(1/2)

    def get_length(self): 
        return self.__length
    def set_pheromone_quantity(self,h=0):
        self.__pheromone_quantity += h
    def get_pheromone_quantity(self):
        return self.__pheromone_quantity
