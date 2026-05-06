class Organism:
    def __init__(self,energy):
        self.__energy= energy  # private vairable 

    @property
    def energy_level(self):
        return self.__energy
    
    @energy_level.setter
    def energy_level(self,energy):
        self.__energy=energy

class plant(Organism):
    
    def energy(self):
        pass


class animal(Organism):

    def energy(self):
        pass

class herbivore(animal):

    def energy(self):
        pass

class omnivore(animal):

    def energy(self):
        pass
    
