from provincia import  Provincia

class Pais (Provincia):
    lista_provincias=[]

    def __init__(self):
        self.lista_provincias=[]

    def AgregarProvincia(self, provincia):
        self.lista_provincias.append(provincia)



