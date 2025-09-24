## Archivo: algoritmos/bfs.py

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        """Agrega un elemento al final de la cola (FIFO)"""
        self.elementos.append(item)

    def desencolar(self):
        """Remueve y retorna el primer elemento de la cola (FIFO)
        None = esta vacia"""
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        """ Indica si la cola se encuentra vacía """
        return len(self.elementos) == 0

    def longitud(self):
        """ Retorna la cantidad de elementos en la cola """
        return len(self.elementos)


def buscar(grafo, inicio, meta):
#      ANALIZAR, COMPRENDER Y EXPLICAR
    frontera = Cola()
    frontera.encolar([inicio])
    visitados = []

    while not frontera.esta_vacia():
        camino = frontera.desencolar()
        nodo = camino[-1]

        if nodo == meta:
            return camino

        if nodo not in visitados:
            visitados.append(nodo)
            for vecino, peso in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                frontera.encolar(nuevo_camino)

    return None
