from classes.City import City
from classes.Road import Road

class Grid:
    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width
        self.__cities: list[City] =  []
        self.__roads: list[Road] = []

    def add_city(self, city: City):
        if not(0 <= city.get_position().x_coordinate <= self.__length) or not(0 <= city.get_position().y_coordinate <= self.__width):
            raise Exception("Impossible to add a city out of the grid")
        elif city in self.__cities:
            raise Exception("Impossible to add a city already in the grid")
        self.__cities.append(city)

    def get_cities(self):
        return self.__cities

    def create_road(self, city1: City, city2: City):
        if (city1 not in self.__cities) or (city2 not in self.__cities):
            raise Exception("Impossible to add a road when one or more of the cities is not in the grid")
        self.__roads.append(Road(city1, city2))

    def get_roads(self):
        return self.__roads