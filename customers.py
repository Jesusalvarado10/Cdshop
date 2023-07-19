from user import User

class Customers(User):

    rol= "Trabajador"

    def __init__(self, name, last_name, dni):
        super().__init__(name, last_name, dni)
    
    def show_atributes(self):
        print(f"{self.rol},{self.name},{self.last_name},{self.dni}")


