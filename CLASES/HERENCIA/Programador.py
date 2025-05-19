from Usuario import Usuario

class Programador(Usuario):

    def __init__(self, first_name, last_name, languaje, payment):
        super().__init__(first_name, last_name)
        self.lang = languaje
        self.payment = payment

    def __str__(self):
        return super().__str__()+" lang "+self.lang + " payment "+str(self.payment)
    
prog1 = Programador("Guido","Lopez","Python",10000.50)
prog2 = Programador("Carlos", "Robertson","C++",20.00)
prog3 = Programador("Edson", "Ruelas","PHP",20000.00)

listP = [prog1,prog2,prog3]

for programmer in listP:
    print(programmer)