class Humano:
    def __init__(self, nombre, color_cabello, nacionalidad):
        self.brazos = 2
        self.pies = 2
        self.nombre = nombre
        self.edad = 0
        self.ojos = 2
        self.orejas = 2
        self.boca = 1
        self.color_cabello = color_cabello
        self.nacionalidad = nacionalidad
        self.nariz = 1
        self.manos = 2

    def comer(self):
        pass

    def pensar(self):
        pass

    def hablar(self):
        print("Hola")

    def correr(self):
        pass

    def respirar(self):
        pass


#humano1 = Humano("Daniel", "Rubio", "Europeo")
#
#print(humano1)
#print(humano1.nombre)