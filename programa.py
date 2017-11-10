from clases.barrios import Barrio
from clases.ciudad import Ciudad
from clases.provincia import Provincia
from clases.pais import Pais
from clases.continente import Continente


un_barrio=Barrio()
otro_barrio=Barrio()
tercer_barrio=Barrio()
cuarto_barrio=Barrio()
quinto_barrio=Barrio()
sexto_barrio=Barrio()


otro_barrio.poblacion=60
un_barrio.poblacion=30
tercer_barrio.poblacion=25
cuarto_barrio.poblacion=10
quinto_barrio.poblacion=33
sexto_barrio.poblacion=65

una_ciudad=Ciudad()
una_ciudad.setNombre("Budapest")
una_ciudad.AgregarBarrio(un_barrio)
una_ciudad.AgregarBarrio(otro_barrio)

otra_ciudad=Ciudad()
otra_ciudad.setNombre("Venado Tuerto")
otra_ciudad.AgregarBarrio(tercer_barrio)
otra_ciudad.AgregarBarrio(cuarto_barrio)

tercer_ciudad=Ciudad()
tercer_ciudad.setNombre("Buenos Aires")
tercer_ciudad.AgregarBarrio(cuarto_barrio)
tercer_ciudad.AgregarBarrio(quinto_barrio)

cuarta_ciudad=Ciudad()
cuarta_ciudad.setNombre("Santiago")
cuarta_ciudad.AgregarBarrio(quinto_barrio)
cuarta_ciudad.AgregarBarrio(sexto_barrio)


una_provincia=Provincia()
una_provincia.setNombre("Santa Cruz")
una_provincia.AgregarCiudad(una_ciudad)
una_provincia.AgregarCiudad(otra_ciudad)

segunda_provincia=Provincia()
segunda_provincia.setNombre("Chaco")
segunda_provincia.AgregarCiudad(una_ciudad)

tercer_provincia=Provincia()
tercer_provincia.setNombre("Misiones")
tercer_provincia.AgregarCiudad(tercer_ciudad)

cuarta_provincia=Provincia()
cuarta_provincia.setNombre("La Rioja")
cuarta_provincia.AgregarCiudad(cuarta_ciudad)

un_pais=Pais()
un_pais.setNombre("Argentina")
un_pais.AgregarProvincia(una_provincia)

otro_pais=Pais()
otro_pais.setNombre("Alemania")
otro_pais.AgregarProvincia(segunda_provincia)

tercer_pais=Pais()
tercer_pais.setNombre("Brasil")
tercer_pais.AgregarProvincia(tercer_provincia)
tercer_pais.AgregarProvincia(cuarta_provincia)

un_continente=Continente()
un_continente.setNombre("America")
un_continente.AgregarPais(un_pais)
un_continente.AgregarPais(otro_pais)

segundo_continente=Continente()
segundo_continente.setNombre("Europa")
segundo_continente.AgregarPais(tercer_pais)



print(un_continente.pais_mas_poblado())
print(un_continente.pais_menos_poblado())


lista_continentes=[]


def agregar_continentes(continente):
    lista_continentes.append(continente)

def continente_mas_poblado():
    maximo = 0
    for item in lista_continentes:
        if maximo == 0:
            maximo = item.Calcular_habitantes_continente()
            nombre = item.devolver_nombre()
        if item.Calcular_habitantes_continente() > maximo:
            maximo = item.Calcular_habitantes_continente()
            nombre = item.devolver_nombre()

    return nombre


def continente_menos_poblado():
    minimo = 0
    for item in lista_continentes:
        if minimo == 0:
            minimo = item.Calcular_habitantes_continente()
            nombre = item.devolver_nombre()
        if item.Calcular_habitantes_continente() < minimo:
            minimo = item.Calcular_habitantes_continente()
            nombre = item.devolver_nombre()

    return nombre


agregar_continentes(un_continente)
agregar_continentes(segundo_continente)
print(continente_mas_poblado())
print(continente_menos_poblado())


