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
        time, cycle_number = 0 , 0 
        etat= False
        for r in self.__road : 
            r.valeur_phero= depot_init #initial deposit of pheromone on all of the track modifier le bail
        while cycle_number< cycle_number_max and etat :#definir cycle number
            for i in self.__ants_list:
                i.set_position(rd.choice(self.__list_cities))
            while len(self.__ants_list[-1].get_route()) < len(self.__cities):
                for i in self.__ants_list : 
                    L= choisir(self,i)
                    i.set_position(L[0])
                    i.set_length_road(i.get_length_road()+L[1])
            etat =  etat_stagnation(self.__ants_list)
            for i in self.__ant_list : 
                actualisation_pheromone(self, i)
                i.reset_route()
            time += len(self.__cities)
            cycle_number+=1

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
        p=Ant.get_position()
        R=Ant.get_route()
        A= Ant.accessible_city
        for i in range(len(A)):
            if A[i] in R:
                R.remove(A[i])
        l_length=[0 for j in range(len(R))]
        l_phero=[0 for j in range(len(R))]
        for i in self.__road:
            for j in range(len(R)):
                if [p,R[j]]== i.get_cities():
                    l_length[j]= i.get_length()
                    l_phero[j]= i.get_pheromone_quantity()
        probability=[0]
        probality_total=0
        for i in range(len(l_length)):
            probality_total+=l_phero(i)**self.__alpha * (1/l_length[i])**self.__beta
            probability.append(probability[-1]+l_phero(i)**self.__alpha * (1/l_length[i])**self.__beta)
        probability=list(map(lambda x : x*probality_total,probability))
        k=proba(probability)  
        return  [R[k],l_length[k]]
            

    def proba(L):
        c=rd.random()
        i=0
        while c>L[i]:
            i+=1

        return i-1

    def accessible_city(self, City):
        L = []
        for R in self.__roads() : 
            A= R.get.cities()
            if City == A[0] :
                L.append(A[1])
            if City == A[1]:
                L.append(A[0])
        return L

    def drop_phero(self, Ant):
        a=Ant.length_road()
            













