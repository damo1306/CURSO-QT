class Airplane():
    def __init__(self, speed, placa):
        self.speed = speed
        self.placa = placa

avionUno = Airplane(235, "JJG6087")
print("------ AVION UNO -------")
print(avionUno.speed, avionUno.placa)

avionDos = Airplane(100, "JPD8083")
print("------ AVION DOS -------")
print(avionDos.speed, avionDos.placa)

