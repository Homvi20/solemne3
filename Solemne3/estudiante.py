from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre="",edad=""):
        super().__init__(nombre,edad)


    def __str__(self):
        return super().__str__()