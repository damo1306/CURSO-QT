#Clase padre
class Animal:
    pass
#Clase hija hereda de padre
class Perro(Animal):
    pass

class Gato(Animal):
    pass

print(Animal.__subclasses__())
print(Perro.__bases__)