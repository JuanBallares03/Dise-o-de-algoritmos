import requests

# -------------------------------
# Clase para representar nodos del grafo Pokémon
# -------------------------------
class Node:
    def __init__(self, name):
        self.name = name
        self.evolves_to = []

# -------------------------------
# Clase principal del grafo Pokémon
# -------------------------------
class PokeGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)
        return self.nodes[name]

    def add_edge(self, origin_name, dest_name):
        origin = self.add_node(origin_name)
        destination = self.add_node(dest_name)
        origin.evolves_to.append(destination)

    def build_from_api(self, chain):
        """Construye el grafo de forma recursiva desde la PokéAPI"""
        origin = chain["species"]["name"]
        for evo in chain["evolves_to"]:
            dest = evo["species"]["name"]
            self.add_edge(origin, dest)
            self.build_from_api(evo)

    def print_graph(self):
        """Muestra la lista de adyacencia"""
        print("📘 Grafo de evolución:")
        for name, node in self.nodes.items():
            evolutions = [e.name for e in node.evolves_to]
            print(f"{name} -> {evolutions}")

    def get_sorted_names(self):
        """Devuelve una lista ordenada alfabéticamente de los nombres"""
        return sorted(self.nodes.keys())


# -------------------------------
# Clase para la búsqueda binaria recursiva
# -------------------------------
class BinarySearch:
    @staticmethod
    def search(lista, objetivo, izquierda=0, derecha=None):
        if derecha is None:
            derecha = len(lista) - 1

        # Caso base: rango inválido
        if izquierda > derecha:
            return False

        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            return BinarySearch.search(lista, objetivo, medio + 1, derecha)
        else:
            return BinarySearch.search(lista, objetivo, izquierda, medio - 1)


# -------------------------------
# Clase principal que controla todo el flujo
# -------------------------------
class PokemonApp:
    def __init__(self, url):
        self.url = url
        self.graph = PokeGraph()

    def run(self):
        print("📡 Obteniendo datos de la PokéAPI...")
        data = requests.get(self.url).json()

        # Construir el grafo
        self.graph.build_from_api(data["chain"])
        self.graph.print_graph()

        # Obtener lista ordenada
        lista_ordenada = self.graph.get_sorted_names()
        print("\n📋 Lista ordenada:", lista_ordenada)

        # Pruebas de búsqueda
        test1 = "ivysaur"
        test2 = "charmander"

        print(f"\n🔍 ¿Está '{test1}' en la cadena?: {BinarySearch.search(lista_ordenada, test1)}")
        print(f"🔍 ¿Está '{test2}' en la cadena?: {BinarySearch.search(lista_ordenada, test2)}")


# -------------------------------
# Ejecución principal
# -------------------------------
if __name__ == "__main__":
    URL = "https://pokeapi.co/api/v2/evolution-chain/1/"
    app = PokemonApp(URL)
    app.run()
