import pytest
import sys
from classes.City import City
from classes.Position import Position

def test_city_attributes():
    city = City("Vienne", Position(100, 32))

    assert city.get_name() == "Vienne", "city attributes test failed"
    assert city.get_position().x_coordinate == 100
    assert city.get_position().y_coordinate == 32

# test_get_roads ?