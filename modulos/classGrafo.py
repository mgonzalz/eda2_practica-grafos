class Ciudad(object):
    def __init__(self,nombre):
        self.nombre = nombre
        self.conexiones = {}

    def agregar_conexion(self, ciudad, peso):
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

if __name__ == '__main__':
    g = Grafo()

    for letra in map(chr, range(65,70)):
        g.agregar_ciudad(Ciudad(letra))

    conexiones_pesos = [
        ('E', 'C', 2),
        ('E', 'D', 3),
        ('C', 'A', 1),
        ('C', 'E', 4),
        ('D', 'A', 2),
        ('D', 'B', 1),
        ('D', 'E', 3),
        ('A', 'B', 5),
        ('A', 'C', 2),
        ('A', 'D', 4),
        ('B', 'A', 1),
        ('B', 'D', 3)
    ]

    for conexion in conexiones_pesos:
        g.agregar_conexion(*conexion)

    g.imprimir_grafo()
