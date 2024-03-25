import pytest
from classes.Road import Road
from classes.City import City
from classes.Position import Position
from classes.Grid import Grid

def test_add_city():
    grid = Grid(100, 100)
    city = City("Vienne", Position(20, 20))
    city_out_of_bounds = City("Givors", Position(120, 20))

    grid.add_city(city)
    assert city in grid.get_cities()

    with pytest.raises(Exception, match="Impossible to add a city out of the grid"):
        grid.add_city(city_out_of_bounds)

def test_create_road():
    grid = Grid(100, 100)
    city1 = City("Vienne", Position(20, 20))
    city2 = City("Givors", Position(20, 40))
    grid.add_city(city1)
    grid.add_city(city2)

    with pytest.raises(Exception, match="Impossible to add a road when one or more of the cities is not in the grid"):
        grid.create_road(city1, City("Lyon", Position(100, 30)))

    grid.create_road(city1, city2)
    assert grid.get_roads()[0].get_cities() == [city1, city2]
    
    
