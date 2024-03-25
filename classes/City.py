from dataclasses import dataclass
from classes.Position import Position

@dataclass
class City:
    __name: str
    __position: Position

    def getRoads(self):
        # à supprimer ?
        pass

    def get_name(self):
        return self.__name
    
    def get_position(self):
        return self.__position