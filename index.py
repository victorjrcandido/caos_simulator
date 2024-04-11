import random

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.rack = {}
        self.restart()
    
    def restart(self):
        self.rack = {i: i for i in self.halteres}    

    def listar(self):
        return [i for i in self.rack.values if i != 0]
    def take(self, peso):
        halter_pos = list(self.rack.values()).index(peso)
        key_halter = list(self.rack.keys())[halter_pos]
        self.rack[key_halter] = 0
        return peso
        
    def devolver(self, pos, peso):
        self.rack[pos] = peso

    def caos(self):
        num_caos = [i for i, j in self.rack.items() if i != j]
        return len(num_caos) / len(self.rack)


self = Academia()


print(self.caos())
