import heapq
from classBST import BSTNode
class Ciudad(object):
    def __init__(self,nombre):
        self.nombre = nombre
        self.conexiones = {}

    def agregar_conexion(self, ciudad, peso):
        self.conexiones[ciudad] = peso

class Grafo(object):
    ciudades = {}
    distancias_bst = BSTNode()
    aristas = []

    def agregar_ciudad(self, ciudad):
        self.ciudades[ciudad.nombre] = ciudad

    def agregar_conexion(self, ciudad1, ciudad2, peso):
        self.ciudades[ciudad1].agregar_conexion(ciudad2, peso)
        self.ciudades[ciudad2].agregar_conexion(ciudad1, peso)

        self.agregar_distancia_bst(peso, ciudad1, ciudad2)
        self.aristas.append((ciudad1, ciudad2, peso))

    def imprimir_grafo(self):
        for nombre, ciudad in sorted(self.ciudades.items()):
            print(f"{nombre} -> {ciudad.conexiones}")


    def dijkstra(self, inicio, destino):
        distancias = {ciudad: float('inf') for ciudad in self.ciudades}
        distancias[inicio] = 0
        cola_prioridad = [{0, inicio}]
        while cola_prioridad:
            distancia_actual, ciudad_actual = heapq.heappop(cola_prioridad)
            if distancia_actual > distancias[ciudad_actual]:
                continue
            for ciudad_vecina, peso in self.ciudades[ciudad_actual].conexiones.items():
                distancia_nueva = distancia_actual + peso
                if distancia_nueva < distancias[ciudad_vecina]:
                    distancias[ciudad_vecina] = distancia_nueva
                    heapq.heappush(cola_prioridad, (distancia_nueva, ciudad_vecina))
        return distancias[destino]


    def agregar_distancia_bst(self, distancia, ciudad1, ciudad2):
        self.distancias_bst.insert(distancia, ciudad1, ciudad2)

    def mostrar_registro_ordenado(self):
        return self.distancias_bst.inorder_traversal()


    def encontrar(self, padre, i):
        if padre[i] == i:
            return i
        return self.encontrar(padre, padre[i])

    def unir(self, padre, rango, x, y):
        xraiz = self.encontrar(padre, x)
        yraiz = self.encontrar(padre, y)

        if rango[xraiz] < rango[yraiz]:
            padre[xraiz] = yraiz
        elif rango[xraiz] > rango[yraiz]:
            padre[yraiz] = xraiz
        else:
            padre[yraiz] = xraiz
            rango[xraiz] += 1

    def KruskalMST(self):
        resultado = []
        self.aristas = sorted(self.aristas, key=lambda item: item[2])

        padre = {}
        rango = {}

        for inicio, destino, distancia in self.aristas:
            padre[inicio] = inicio
            padre[destino] = destino
            rango[inicio] = 0
            rango[destino] = 0

        for inicio, destino, distancia in self.aristas:
            x = self.encontrar(padre, inicio)
            y = self.encontrar(padre, destino)

            if x != y:
                resultado.append([inicio, destino, distancia])
                self.unir(padre, rango, x, y)

        coste_min = 0
        print("Aristas en el MST:")
        for inicio, destino, distancia in resultado:
            coste_min += distancia
            print(f"{inicio} - {destino}: {distancia}")
        print("Minimum Spanning Tree:", coste_min)




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
    print('\n')

    inicio = 'A'
    destino = 'E'
    distancia_minima = g.dijkstra(inicio, destino)
    print(f"La distancia minima entre {inicio} y {destino} es {distancia_minima}\n")

    registro = g.mostrar_registro_ordenado()
    for distancia, ciudad1, ciudad2 in registro:
        print(f'Distancia {distancia} entre {ciudad1} y {ciudad2}')

    print('\n')
    g.KruskalMST()
