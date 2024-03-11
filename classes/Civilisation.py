from dataclasses import dataclass
from classes.City import City
from classes.Road import Road
from classes.Ant import Ant
import random as rd
RATE = 0.2

@dataclass
class Civilisation:
    __cities: list[City]
    __roads: list[Road]
    __ants_list: list[Ant]
    __ants_number: int
    __start_city: City
    __nb_iterations: int

    def start(self):

        for iteration in range(self.__nb_iterations):
            self.__ants_list = self.generate_ants()

            for step in range(len(self.__cities)):
                self.next()

    def next(self):
        for ant in self.__ants_list:
            # calcul des différentes probas avec les routes dispos
            # nouvelle ville = city
            # availabe_cities = [for road in self.__roads if ]
            city = 0
            ant.move(city)

    def generate_ants(self):
        return [Ant(self.__start_city, [], RATE) for i in range(self.__ants_number)]


def tsp(self): 
    time, cycle_number = 0 , 0 
    for r in self.__road : 
        r.valeur_phero= depot_init

    for i in self.__ants_list:
        i.set_position(rd.choice(self.__list_cities))
    while len(self.__ants_list[-1].get_route()) < len(self.__cities):
        for i in self.__ants_list : 
            a= choisir(self,i)
            i.set_position(a)

def choisir(self, Ant):
    p=Ant.get_position()
    R=Ant.get_route()
    A= Ant.accessible_city
    for i in range(len(A)):
        if A[i] in R:
            del A[i]
    
    
def accessible_city(self, City):
    for R in self.__roads() : 
        












