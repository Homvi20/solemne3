from persona import Persona

class Docente(Persona):
    def __init__(self, nombre="",edad="",sueldo=""):
        super().__init__(nombre,edad)
        self.__sueldo=sueldo


    def __str__(self):
        return super().__str__()+ - "Sueldo: {}".format(self.__sueldo)


    def GetSueldo(self):
        return self.__sueldo

    def SetSueldo(self,sueldo):
        self.__sueldo=sueldo