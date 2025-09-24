## Archivo: algoritmos/ucs.py

class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def insertar(self, elemento):
        """Inserta un elemento (costo, camino) manteniendo orden por costo minimo"""

        self.elementos.append(elemento)
        self.elementos.sort(key=lambda x: x[0])

    def sacar(self):
        """Remueve y retorna el elemento con menor costo (primer elemento)
        None == esta vacia"""

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
    frontera = ColaPrioridad()
    frontera.insertar((0, [inicio]))
    visitados = []

    while not frontera.esta_vacia():
        costo, camino = frontera.sacar()
        nodo = camino[-1]

        if nodo == meta:
            return camino

        if nodo not in visitados:
            visitados.append(nodo)
            for vecino, peso in grafo.get(nodo, []):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    frontera.insertar((costo + peso, nuevo_camino))

    return None
