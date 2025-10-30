# main.py
from grafo import Graph
from mapsUtils import Busqueda_Ruta

# ==== Entrada desde consola ====
origen = input("Escribe el origen: ").strip()
destino = input("Escribe el destino: ").strip()
paradas = input("Escribe las paradas separadas por coma (si hay): ").strip().split(',')
paradas = [p.strip() for p in paradas if p.strip() != ""]

# ==== Construcción del grafo ====
g = Graph()
g.add_node(origen)
for p in paradas:
    g.add_node(p)
g.add_node(destino)

# Conectar los nodos según el orden
ruta = [origen] + paradas + [destino]
for i in range(len(ruta) - 1):
    g.connect(ruta[i], ruta[i + 1])

# ==== Mostrar las conexiones creadas ====
print("\nRuta generada:")
for name, node in g.nodes.items():
    print(f"Nodo {name} conectado con:", end=" ")
    if node.edges:
        print(", ".join(edge.destination.name for edge in node.edges))
    else:
        print("ninguno")

# ==== Abrir Google Maps ====
Busqueda_Ruta(origen, destino, paradas)
