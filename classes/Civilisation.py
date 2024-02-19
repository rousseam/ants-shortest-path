from dataclasses import dataclass
from classes.City import City

@dataclass
class Civilisation:
    name: str
    nest: City
    food: City

    def start(self):
        pass

    def next(self):
        pass