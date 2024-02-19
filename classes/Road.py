from dataclasses import dataclass
from City import City

@dataclass
class Road:
    pheromone_qtity: float
    length: int
    city1: City
    city2: City

    def evaporate_pheromone(self):
        pass
