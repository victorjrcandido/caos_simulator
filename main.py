import random
import seaborn as sns
class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.rack = {}
        self.restart()
    
    def restart(self):
        self.rack = {i: i for i in self.halteres}    

    def listar_halteres(self):
        return [i for i in self.rack.values() if i != 0]
    
    def listar_espacos(self):
        return [i for i, j in self.rack.items() if j == 0]

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

class User():
    def __init__(self, tipo, academia):
        self.tipo = tipo # 1 = normal, 2 = random
        self.academia = academia
        self.peso = 0
    
    def start(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.take(self.peso)

    def end(self):
        espacos = self.academia.listar_espacos()

        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver(pos, self.peso)    

        if self.tipo == 2:
                pos = random.choice(espacos)
                self.academia.devolver(pos, self.peso)
        self.peso = 0


academia = Academia()

users = [User(1, academia) for i in range(10)]
users += [User(2, academia) for i in range(1)]
random.shuffle(users)

list_caos = []

for k in range(10):
    academia.restart()
    for i in range(10):
        random.shuffle(users)
        for user in users:
            user.start()
        for user in users:
            user.end()
    list_caos += [academia.caos()]

# sns.histplot(list_caos, kde=True)

print(list_caos)
