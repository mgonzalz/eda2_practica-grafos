# Práctica de grafos: Red de Transporte.

## Repositorio.
- Integrantes del grupo: Jacobo Calviño (@Jacobo24), Lucia Cantos (@luciacantos), María González (@mgonzalz).
- Link: https://github.com/mgonzalz/eda2_practica-grafos.git
## Enunciado.
Se te ha encargado crear un sistema para optimizar la red de transporte entre ciudades.
Debes modelar este problema como un grafo donde cada nodo representa una ciudad y
cada arista representa una conexión entre dos ciudades. Cada arista tiene asociado un
peso que representa la distancia entre las ciudades. <br>
Además, se requiere mantener un registro ordenado de las distancias entre ciudades. Para
esto, se debe utilizar un árbol binario de búsqueda (BST) donde las claves sean las
distancias y los valores sean las ciudades conectadas por esa distancia. <br>
Se te pide implementar lo siguiente:
- Una clase Grafo que represente el grafo de ciudades y sus conexiones. Debe
permitir añadir ciudades, agregar conexiones entre ellas con sus respectivos pesos y
mostrar el grafo resultante.
- Un método para encontrar la ruta más corta entre dos ciudades. Deberás
implementar una función `ruta_mas_corta(origen, destino)` que devuelva la ruta
más corta entre las ciudades origen y destino (el camino de ciudades recorridas),
junto con la distancia total de esa ruta.
- Integrar un BST para mantener un registro ordenado de las distancias entre
ciudades. Implementa funciones para agregar una nueva distancia con sus ciudades
correspondientes y para mostrar el registro ordenado.
- Un método que seleccione una colección de aristas tal que el grafo quede conectado
y la suma de las distancias sea mínima (Árbol de recubrimiento mínimo).

Consideraciones:

- Puedes representar el grafo utilizando una matriz de adyacencia o listas de
adyacencia.
- Las ciudades pueden ser representadas por números o nombres.
- Proporciona ejemplos de uso de tu implementación con un conjunto de ciudades y
sus conexiones.

