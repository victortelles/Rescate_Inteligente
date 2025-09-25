## Archivo: algoritmos/greedy.py

class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def insertar(self, elemento):
        h_nuevo = elemento[0]
        insertado = False
        for i in range(len(self.elementos)):
            if h_nuevo < self.elementos[i][0]:
                self.elementos.insert(i, elemento)
                insertado = True
                break
        if not insertado:
            self.elementos.append(elemento)

    def sacar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def longitud(self):
        return len(self.elementos)


def h(n, heuristica, meta):
    x1, y1 = heuristica[n]
    x2, y2 = heuristica[meta]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def buscar(grafo, inicio, meta, heuristica):
    frontera = ColaPrioridad()
    frontera.insertar((h(inicio, heuristica, meta), [inicio]))
    visitados = []

    while not frontera.esta_vacia():
        heur, camino = frontera.sacar()
        nodo = camino[-1]

        if nodo == meta:
            return camino

        if nodo not in visitados:
            visitados.append(nodo)
            for vecino, _ in grafo.get(nodo, []):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    heuristica_vecino = h(vecino, heuristica, meta)
                    frontera.insertar((heuristica_vecino, nuevo_camino))

    return None
