#clase padre
class Animal:
    #Constructor
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def hablar():
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

#clase hija hereda animal
class Perro(Animal):
    def hablar(self):
        print("Guau")
    def moverse(self):
        print("En 5 patas")

class Gato(Animal):
    def hablar(self):
        print("Miau")
    def moverse(self):
        print("En 4 patas")

gato = Gato("mamifero",10)
perro = Perro("mamifero",5)

gato.hablar()
perro.hablar()

gato.describeme()
perro.describeme()
