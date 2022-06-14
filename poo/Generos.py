from HumanoClase import Humano

class Monstruo:
    super_fuerza = True    

class Mujer(Humano):
    def __init__(self, nombre, color_cabello, nacionalidad):
        super().__init__(nombre, color_cabello, nacionalidad)
        self.genero = 'Femenino'

class Hombre(Humano):
    def __init__(self, nombre, color_cabello, nacionalidad, prostata=True):
        super().__init__(nombre, color_cabello, nacionalidad)
        self.genero = 'Masculino'
        self.prostata = prostata
        self._prostata = 'x'

class HombreMonstruo(Humano, Monstruo):
    def __init__(self, nombre, color_cabello, nacionalidad):
        super().__init__(nombre, color_cabello, nacionalidad)

jorge = Hombre("Jorge","Pelirojo", "Mexicana", False)
edgar = Hombre("Edgar", "Blanco", "Rusa")
jaime = HombreMonstruo("Jaime", "negro", "Marciano")


print("Tiene prostata? :", jorge.prostata)
print("Tiene prostata? :", edgar.prostata)

jorge.hablar()
edgar.hablar()
print(jaime.super_fuerza)

# numpy, pandas