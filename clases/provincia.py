from .ciudad import Ciudad
from .lugar import Lugar

class Provincia (Lugar):
    lista_ciudades=[]

    def __init__(self):
        self.lista_ciudades=[]

    def AgregarCiudad (self, ciudad):
        self.lista_ciudades.append(ciudad)

    def Calcular_habitantes_provincia(self):
        cant=0
        for item in self.lista_ciudades:
            cant=cant+item.Calcular_habitantes_ciudad()
        return cant
