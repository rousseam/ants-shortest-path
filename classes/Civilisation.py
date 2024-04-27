from dataclasses import dataclass
from classes.City import City
from classes.Road import Road
from classes.Ant import Ant
import random as rd
RATE = 0.2
MAX_CYCLE = 1000
PHERO_INIT = 0.1

@dataclass
class Civilisation:
    __cities: list[City]
    __roads: list[Road]
    __ants_list: list[Ant]
    __ants_number: int
    __start_city: City
    __nb_iterations: int
    __alpha : float
    __beta : float
    __rho : float #rate pheromone evaporation

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
        time, cycle_number = 0, 0 
        is_stagnation = False

        for road in self.__roads: 
            road.set_pheromone_quantity(PHERO_INIT) #initial deposit of pheromone on all of the track modifier le bail

        while cycle_number < MAX_CYCLE and is_stagnation: #definir cycle number
            for ant in self.__ants_list:
                ant.set_position(rd.choice(self.__cities))

            while len(self.__ants_list[-1].get_route()) < len(self.__cities):
                for ant in self.__ants_list : 
                    L= self.choisir(self, ant)
                    ant.set_position(L[0])
                    ant.set_travel_length(ant.get_travel_length() + L[1])
            is_stagnation =  self.etat_stagnation(self.__ants_list)

            for ant in self.__ants_list :
                self.actualisation_pheromone(self, ant)
                ant.reset_route()

            time += len(self.__cities)
            cycle_number += 1

    def etat_stagnation(self,list_ant):
        route = list_ant[0].get_route()
        for i in list_ant : 
            if i.get_route() != route : 
                return True
        return False

    def actualisation_pheromone(self,Ant):
        R=Ant.get_route()    
        phero_drop= self.__Q /Ant.get_length_road()

        for i in range(len(R)-1):
            for j in self.__roads:
                if j.get_cities == [R[i],R[i+1]]:
                    j.set_pheromone_quantity(j.get_pheromone_quantity*phero_drop* self.__rho)


    def choisir(self, Ant: Ant):
        position = Ant.get_position()
        ant_path = Ant.get_route()
        accessible_roads: list[Road] = Ant.accessible_city # à modifier
        for road_accessible in accessible_roads:
            if road_accessible in ant_path:
                ant_path.remove(road_accessible)
        l_length = [0 for j in range(len(road_accessible))]
        l_phero = [0 for j in range(len(road_accessible))]

        for road in self.__roads:
            for j in range(len(road_accessible)):
                if [position, road_accessible[j]] == road.get_cities():
                    l_length[j] = road.get_length()
                    l_phero[j] = road.get_pheromone_quantity()

        probability=[0]
        probality_total=0

        for i in range(len(l_length)):
            probality_total+=l_phero(i)**self.__alpha * (1/l_length[i])**self.__beta
            probability.append(probability[-1] + l_phero(i)**self.__alpha * (1/l_length[i])**self.__beta)

        probabilities=list(map(lambda x : x*probality_total,probability))
        k = self.proba(probabilities)  
        return  [accessible_roads[k], l_length[k]]
            

    def proba(probabilities):
        p = rd.random()
        i = 0
        while p > probabilities[i]:
            i += 1

        return i - 1

    def accessible_city(self, city):
        accessible_cities = []
        for road in self.__roads : 
            cities = road.get_cities()
            if city == cities[0] :
                accessible_cities.append(cities[1])
            if city == cities[1]:
                accessible_cities.append(cities[0])
        return accessible_cities
            













