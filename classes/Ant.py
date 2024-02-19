from dataclasses import dataclass

@dataclass
class Ant:
    alpha: int
    beta: int
    gamma: int
    isCarryingFood: bool

    def move(self):
        pass

    def drop_pheromone(self):
        pass