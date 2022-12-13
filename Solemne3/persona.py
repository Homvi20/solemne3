class Persona():
    def _init_(self,nombre="", edad=""):
        self.__nombre=nombre
        self.__edad=edad

    def __str__(self):
        return "Nombre: {} - Edad: {}".format(self.__nombre,self.__edad)

    def GetNombre(self):
        return self.__nombre
    def GetEdad(self):
        return self.__edad

    def SetNombre(self,n):
        self.__nombre=n
    def SetEdad(self,edad):
        self.__edad=edad
    
