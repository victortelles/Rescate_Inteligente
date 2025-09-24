import matplotlib.pyplot as plt
import networkx as nx

def dibujar_grafo_con_camino(grafo, posiciones, camino, inicio, meta):
    G = nx.Graph()
    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            G.add_edge(nodo, vecino, weight=peso)
    pos = posiciones
    nx.draw(G, pos, with_labels=True, node_color='lightblue')
    if camino:
        path_edges = list(zip(camino, camino[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=[inicio], node_color='green')
        nx.draw_networkx_nodes(G, pos, nodelist=[meta], node_color='red')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='orange', width=2)
    plt.title("Camino encontrado")
    plt.show()
