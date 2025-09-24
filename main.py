from algoritmos import bfs, ucs, astar
from utils.grafo_utils import cargar_grafo
from utils.visualizacion import dibujar_grafo_con_camino

def main():
    grafo, inicio, metas, posiciones = cargar_grafo("grafos/ciudad_ejemplo.json")

    print("\n=== Búsqueda de rutas desde el hospital a las zonas de emergencia ===\n")

    for meta in metas:
        print(f"\n--- Buscando ruta a emergencia en {meta} ---")

        camino_bfs = bfs.buscar(grafo, inicio, meta)  # TODO: implementar
        camino_ucs = ucs.buscar(grafo, inicio, meta)  # TODO: implementar
        camino_astar = astar.buscar(grafo, inicio, meta, posiciones)  # TODO: implementar

        print(f"BFS: {camino_bfs}")
        print(f"UCS: {camino_ucs}")
        print(f"A*: {camino_astar}")

        # Visualiza solo el resultado de A* por defecto (se puede cambiar)
        if camino_astar:
            dibujar_grafo_con_camino(grafo, posiciones, camino_astar, inicio, meta)
        else:
            print("No se encontró un camino con A*.")

if __name__ == '__main__':
    main()
