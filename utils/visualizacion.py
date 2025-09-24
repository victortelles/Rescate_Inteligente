import matplotlib.pyplot as plt
import networkx as nx

def dibujar_grafo_con_camino(grafo, posiciones, camino, inicio, meta, algoritmo=None):
    G = nx.Graph()
    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            G.add_edge(nodo, vecino, weight=peso)
    pos = posiciones
    nx.draw(G, pos, with_labels=True, node_color='lightblue')
    # Mostrar los pesos en las aristas
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    if camino:
        path_edges = list(zip(camino, camino[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=[inicio], node_color='green')
        nx.draw_networkx_nodes(G, pos, nodelist=[meta], node_color='red')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='orange', width=2)
    titulo = "Camino encontrado"
    if algoritmo:
        titulo += f" | {algoritmo}"
    plt.title(titulo)
    plt.show()
