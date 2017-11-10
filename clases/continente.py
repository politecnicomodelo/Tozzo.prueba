from .pais import Pais
from .lugar import Lugar

class Continente (Lugar):
    lista_paises=[]

    def __init__(self):
        self.lista_paises=[]

    def AgregarPais(self, pais):
        self.lista_paises.append(pais)

    def Calcular_habitantes_continente(self):
        cant=0
        for item in self.lista_paises:
            cant=cant+item.Calcular_habitantes_pais()

        return cant

    def pais_mas_poblado(self):
        maximo=0
        for item in self.lista_paises:
            if maximo==0:
                maximo=item.Calcular_habitantes_pais()
                nombre=item.devolver_nombre()
            if item.Calcular_habitantes_pais()>maximo:
                maximo=item.Calcular_habitantes_pais()
                nombre=item.devolver_nombre()

        return nombre

    def pais_menos_poblado(self):
        minimo=0
        for item in self.lista_paises:
            if minimo == 0:
                minimo = item.Calcular_habitantes_pais()
                nombre = item.devolver_nombre()
            if item.Calcular_habitantes_pais() < minimo:
                minimo = item.Calcular_habitantes_pais()
                nombre = item.devolver_nombre()

        return nombre

