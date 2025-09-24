from algoritmos import bfs, ucs, astar
from utils.grafo_utils import cargar_grafo
from utils.visualizacion import dibujar_grafo_con_camino

def main():
    print("\n=== Selección de ciudad/mapa ===\n")
    opciones = [
        "ciudad_ejemplo.json",
        "ciudad_costos.json",
        "ciudad_emergencias.json",
        "ciudad_extendido.json"
    ]
    for i, nombre in enumerate(opciones, 1):
        print(f"{i}. {nombre}")
    seleccion = input("Selecciona el número de la ciudad a usar: ")
    try:
        idx = int(seleccion) - 1
        if idx < 0 or idx >= len(opciones):
            raise ValueError
        archivo = f"grafos/{opciones[idx]}"
    except ValueError:
        print("Selección inválida. Se usará ciudad_ejemplo.json por defecto.")
        archivo = "grafos/ciudad_ejemplo.json"

    grafo, inicio, metas, posiciones = cargar_grafo(archivo)

    print("\n=== Búsqueda de rutas desde el hospital a las zonas de emergencia ===\n")

    for meta in metas:
        print(f"\n--- Buscando ruta a emergencia en {meta} ---")

        camino_bfs = bfs.buscar(grafo, inicio, meta)  # TODO: implementar
        camino_ucs = ucs.buscar(grafo, inicio, meta)  # TODO: implementar
        camino_astar = astar.buscar(grafo, inicio, meta, posiciones)  # TODO: implementar

        print(f"BFS: {camino_bfs}")
        print(f"UCS: {camino_ucs}")
        print(f"A*: {camino_astar}")

        # Visualiza el resultado de cada algoritmo
        if camino_bfs:
            dibujar_grafo_con_camino(grafo, posiciones, camino_bfs, inicio, meta, algoritmo="BFS")
        else:
            print("No se encontró un camino con BFS.")
        if camino_ucs:
            dibujar_grafo_con_camino(grafo, posiciones, camino_ucs, inicio, meta, algoritmo="UCS")
        else:
            print("No se encontró un camino con UCS.")
        if camino_astar:
            dibujar_grafo_con_camino(grafo, posiciones, camino_astar, inicio, meta, algoritmo="A*")
        else:
            print("No se encontró un camino con A*.")

if __name__ == '__main__':
    main()
