class Usuario():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        
    def create_mail(self):
        return self.first_name.lower() + "." + self.last_name.lower() + "@"+"gmail.com"
    
    def __str__(self):
        return ("nombre = {} correo = {}".format(self.full_name, self.create_mail()))
    
a = Usuario("Daniel","Morales")
print(a)
