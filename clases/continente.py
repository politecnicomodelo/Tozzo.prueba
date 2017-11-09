from pais import Pais

class Continente (Pais):
    lista_paises=[]

    def __init__(self):
        self.lista_paises=[]

    def AgregarPais(self, pais):
        self.lista_paises.append(pais)