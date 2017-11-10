class Lugar (object):
    nombre= None
    codigo = None
    lista_coordenadas = [ ]

    def __init__(self):
        self.lista_coordenadas=[]

    def setNombre (self, nombre):
        self.nombre=nombre

    def setCodigo (self, codigo):
        self.codigo=codigo

    def AgregarCoordenada(self, coordenada):
        self.lista_coordenadas.append(coordenada)

    def devolver_nombre(self):
        return self.nombre

