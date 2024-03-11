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


def tsp(Civilisation): 
    time, cycle_number = 0 , 0 
    for r in Civilisation.__road : 
        r.valeur_phero= depot_init

    for i in Civilisation.__ants_list:
        i.set_position(rd.choice(Civilisation.__list_cities))
    while len(Civilisation.__ants_list[-1].get_route()) < len(Civilisation.__cities):
        for i in Civilisation.__ants_list : 
            a= choisir(Civilisation,i)
            i.set_position(a)
    
def choisir(Civilisation, Ant):
    p=Ant.get_position()
    R=Ant.get_route()
    A= Ant.accessible_city
    for i in range(len(A)):
        if A[i] in R:
            del A[i]
    
    













