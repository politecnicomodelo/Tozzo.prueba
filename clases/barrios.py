from lugar import Lugar
class Barrio (Lugar):
    poblacion=0
    def __init__(self):
        self.poblacion=0

    def CantidadPoblacion(self):
        return self.poblacion
