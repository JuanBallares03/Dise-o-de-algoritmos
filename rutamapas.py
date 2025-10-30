# ==== Importar para abrir Google Maps ====
import webbrowser

# ==== Estructura formal de grafo (usando Node y Edge) ====
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []  # Lista de aristas (Edge)

class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def connect(self, origin_name, destination_name):
        origin = self.nodes[origin_name]
        destination = self.nodes[destination_name]
        edge = Edge(origin, destination)
        origin.edges.append(edge)

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
print("\nRuta generada (usando Node y Edge):")
for name, node in g.nodes.items():
    print(f"Nodo {name} conectado con:", end=" ")
    if node.edges:
        print(", ".join(edge.destination.name for edge in node.edges))
    else:
        print("ninguno")

# ==== Generar URL de Google Maps ====
url = f"https://www.google.com/maps/dir/?api=1&origin={origen}&destination={destino}"
if paradas:
    url += "&waypoints=" + "|".join(paradas)

print("\nAbriendo Google Maps con la ruta...")
webbrowser.open(url)
