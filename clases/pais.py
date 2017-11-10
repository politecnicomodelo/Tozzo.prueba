from .provincia import  Provincia
from .lugar import Lugar

class Pais (Lugar):
    lista_provincias=[]

    def __init__(self):
        self.lista_provincias=[]

    def AgregarProvincia(self, provincia):
        self.lista_provincias.append(provincia)


    def Calcular_habitantes_pais(self):
        cant=0
        for item in self.lista_provincias:
            cant=cant+item.Calcular_habitantes_provincia()
        return cant


