from dataclasses import dataclass
from classes.Position import Position

@dataclass
class City:
    __name: str
    __position: Position

    def getRoads(self):
        pass