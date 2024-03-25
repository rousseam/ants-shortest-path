import pytest
from classes.Road import Road
from classes.City import City
from classes.Position import Position

def test_road_length():
    road = Road(City("Vienne", Position(20, 20)), City("Givors", Position(20, 40)))

    assert road.get_length() == 20