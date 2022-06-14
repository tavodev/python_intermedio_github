
class Animal:
    def __init__(self, tipo):
        self.tipo = tipo

    def comer(self):
        print("comiendo")


perro = Animal("perro")

print(perro.tipo)
perro.comer()