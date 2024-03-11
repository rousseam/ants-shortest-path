from dataclasses import dataclass

@dataclass
class Ant:
    __position : City
    __route : list[City]
    __rate_phero : int
    %isCarryingFood:bool

    def get_position(self):
        return self.__position 
    def set_position(self,City):
        self.__position = City
   
    def get_route(self):
        return self.__route
    def reset_route(self):
        self.__route=[]    
    
    def move(self, City):
        self.__route.append(City)
