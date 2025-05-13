class Madre:
    def __init__(self):
        print("Soy madre")

class Padre:
    def __init__(self):
        print("Soy padre")

class Hijo(Madre, Padre):
    def __init__(self):
        #Herencia multiple
        Madre.__init__(self)
        Padre.__init__(self)
        # Heredar
        # super().__init__()
        print("Soy hijo")

hijo = Hijo()