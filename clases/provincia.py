from ciudad import Ciudad

class Provincia (Ciudad):
    lista_ciudades=[]

    def __init__(self):
        self.lista_ciudades=[]

    def AgregarCiudad (self, ciudad):
        self.lista_ciudades.append(ciudad)
