class Ciudad(object):
    def __init__(self,nombre):
        self.nombre = nombre
        self.conexiones = {}

    def agregar_conexion(self, cuidad, peso):
        self.conexiones[ciudad] = peso

class Grafo(object):
    ciudades = {}

    def agregar_ciudad(self, ciudad):
        self.ciudades[ciudad.nombre] = ciudad

    def agregar_conexion(self, ciudad1, ciudad2, peso):
        self.ciudades[ciudad1].agregar_conexion(ciudad2, peso)
        self.ciudades[ciudad2].agregar_conexion(ciudad1, peso)

    def imprimir_grafo(self):
        for nombre, ciudad in sorted(self.ciudades.items()):
            print(f"{nombre} -> {ciudad.conexiones}")

            