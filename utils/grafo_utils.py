import json

def cargar_grafo(ruta):
    with open(ruta, 'r') as f:
        data = json.load(f)
    return data['grafo'], data['inicio'], data['metas'], data['posiciones']
