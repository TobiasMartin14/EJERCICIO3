
class Registro():
    __temperatura = None
    __humedad = None
    __presionAtmosferica = None
    
    def __init__ (self, temperatura, humedad, presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presionAtmosferica = presion
    
    def retornaTemp (self):
        return self.__temperatura
    def retornaHum (self):
        return self.__humedad
    def retornaPre(self):
        return self.__presionAtmosferica
    
