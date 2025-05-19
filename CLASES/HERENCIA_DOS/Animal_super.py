class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un animal del tipo ",type(self).__name__)

class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        self.especie = especie
        self.edad = edad
        self.dueño = dueño

perro = Perro("mamifero",7,"juan")
print(perro.especie, perro.edad, perro.dueño)