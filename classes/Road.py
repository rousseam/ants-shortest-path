from dataclasses import dataclass

@dataclass
class Road:
    __pheromone_qtity: float
    __length: float =0
    __starting_city: City
    __ending_city : City

    def set_length(self): 
        self.__length = (self.__starting_city.)