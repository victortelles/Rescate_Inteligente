class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def insertar(self, elemento):
        """Inserta (f, g, camino) manteniendo orden por valor f minimo
        f = g + h donde g es costo acumulado y h es heuristica"""

        self.elementos.append(elemento)
        self.elementos.sort(key=lambda x: x[0])

    def sacar(self):
        """Remueve y retorna el elemento con menor valor f (primer elemento)
        None == esta vacia la cola"""

        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        """Indica si la cola se encuentra vacía"""
        return len(self.elementos) == 0

    def longitud(self):
        """ Retorna la cantidad de elementos en la cola """
        return len(self.elementos)


def h(n, heuristica, meta):
    """Calcula la distancia euclidiana entre el nodo actual y el nodo meta
    Formula: sqrt((x2-x1)^2 + (y2-y1)^2)"""
    x1, y1 = heuristica[n]
    x2, y2 = heuristica[meta]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def buscar(grafo, inicio, meta, heuristica):
#       ANALIZAR, COMPRENDER Y EXPLICAR
    frontera = ColaPrioridad()
    frontera.insertar((h(inicio, heuristica, meta), 0, [inicio]))
    visitados = []

    while not frontera.esta_vacia():
        f, g, camino = frontera.sacar()
        nodo = camino[-1]

        if nodo == meta:
            return camino

        if nodo not in visitados:
            visitados.append(nodo)
            for vecino, costo in grafo.get(nodo, []):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    g_nuevo = g + costo
                    f_nuevo = g_nuevo + h(vecino, heuristica, meta)
                    frontera.insertar((f_nuevo, g_nuevo, nuevo_camino))

    return None
