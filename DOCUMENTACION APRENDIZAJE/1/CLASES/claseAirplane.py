class Airplane():
    #pass #rellena el bloque para evitar errores de sintaxis
    def __init__(self, speed, placa):
        self.speed = speed
        self.placa = placa
        
avion1 = Airplane(5000, "AI1234")
avion2 = Airplane(3000, "BI1234")

print(avion1.placa)
print(avion1.speed)
print(avion2.placa)
print(avion2.speed)