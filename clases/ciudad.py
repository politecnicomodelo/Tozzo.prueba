from barrios import Barrio

class Ciudad(Barrio):
    lista_barrio=[]

    def __init__(self):
        self.lista_barrio=[]

    def AgregarBarrio (self,barrio):
        self.lista_barrio.append(barrio)

    def Calcular_habitantes_ciudad(self):
        for item in self.lista_barrio:
            cant=cant+item.CantidadPoblacion()
        return cant

