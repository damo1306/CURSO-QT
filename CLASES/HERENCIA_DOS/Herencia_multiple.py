class Clase1:
    pass
class Clase2(Clase1):
    pass
class Clase3(Clase2):
    pass
class Clase4(Clase1,Clase2, Clase3):
    pass

print(Clase4.__mro__)
