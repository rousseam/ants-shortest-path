from dataclasses import dataclass
from classes.Position import Position

@dataclass
class City:
    name: str
    position: Position

    def getRoads(self):
        pass