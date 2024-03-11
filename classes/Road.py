from dataclasses import dataclass
from City import City

@dataclass
class Road:
    def __init__(self, city1: City, city2: City):
        self.__city1 = city1
        self.__city2 = city2
        self.__pheromone_quantity = 0
        self.__length = self.set_length(city1, city2)

    def set_length(self): 
        self.__length = ((self.__city1.position.x_coordinate()-self.__city2.position.x_coordinate())**2 - (self.__city1.position.y_coordinate()-self.__city2.position.y_coordinate())**2)**(1/2)

    def get_length(self): 
        return self.__length

    def set_pheromone_quantity(self,h=0):
        self.__pheromone_quantity += h

    def get_pheromone_quantity(self):
        return self.__pheromone_quantity

    def get_cities(self):
        return [self.__city1, self.__city2]