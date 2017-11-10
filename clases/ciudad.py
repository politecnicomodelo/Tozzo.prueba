from .barrios import Barrio
from .lugar import Lugar

class Ciudad(Lugar):
    lista_barrio=[]

    def __init__(self):
        self.lista_barrio=[]

    def AgregarBarrio (self,barrio):
        self.lista_barrio.append(barrio)

    def Calcular_habitantes_ciudad(self):
        cant=0
        for item in self.lista_barrio:
            cant=cant+item.CantidadPoblacion()
        return cant

