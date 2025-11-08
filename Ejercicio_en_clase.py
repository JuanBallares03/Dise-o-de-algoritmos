class Furgoneta:
    def __init__(self, marca, modelo, capacidad_carga, rutas, horas_disponibles, capacidad_actual):
        self.marca = marca
        self.modelo = modelo
        self.capacidad_carga = capacidad_carga
        self.rutas = rutas
        self.horas_disponibles = horas_disponibles
        self.capacidad_actual = capacidad_actual


class Nodos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.Adyacentes = []


class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodos(nombre)
        else:
            print(f"El nodo '{nombre}' ya existe.")

    def agregar_Adyacente(self, origen, destino, distancia, tiempo):
        if origen in self.nodos and destino in self.nodos:
            self.nodos[origen].Adyacentes.append({
                "destino": destino,
                "distancia": distancia,
                "tiempo": tiempo
            })
        else:
            print("Uno o ambos nodos no existen en el grafo.")

    def mostrarConexiones(self):
        print("\nConexiones del grafo:")
        for nombre, nodo in self.nodos.items():
            if nodo.Adyacentes:
                for ady in nodo.Adyacentes:
                    print(f"{nombre} --> {ady['destino']} | Distancia: {ady['distancia']} | Tiempo: {ady['tiempo']}")
            else:
                print(f"{nombre} no tiene conexiones.")

    def buscar_ruta(self, origen, destino):
        if origen not in self.nodos or destino not in self.nodos:
            print("Uno o ambos nodos no existen en el grafo.")
            return None

        visitados = set()
        cola = [(origen, [origen])]

        while cola:
            nodo_actual, ruta = cola.pop(0)

            if nodo_actual == destino:
                return ruta

            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                for ady in self.nodos[nodo_actual].Adyacentes:
                    if ady["destino"] not in visitados:
                        cola.append((ady["destino"], ruta + [ady["destino"]]))

        return None


# --- Objetos Furgoneta ---
Furgoneta1 = Furgoneta("Mazda", "BT-50", 1000, ["Ruta1", "Ruta2"], 8, 100)
Furgoneta2 = Furgoneta("Toyota", "Hilux", 900, ["Ruta3", "Ruta4"], 8, 200)
Furgoneta3 = Furgoneta("Ford", "Ranger", 1100, ["Ruta5", "Ruta6"], 8, 300)
Furgoneta4 = Furgoneta("Nissan", "Navara", 950, ["Ruta7", "Ruta8"], 8, 400)
Furgoneta5 = Furgoneta("Chevrolet", "S10", 1050, ["Ruta9", "Ruta10"], 8, 500)

# --- Inicialización del grafo ---
GrafoRutas = Grafo()

cantidad = int(input("¿Cuántos nodos (ciudades) desea agregar?: "))

for i in range(cantidad):
    nombre_nodo = input(f"Ingrese el nombre del nodo {i+1}: ")
    GrafoRutas.agregar_nodo(nombre_nodo)

print("\nNodos agregados correctamente:")
for nombre in GrafoRutas.nodos:
    print(f"- {nombre}")

# --- Agregar conexiones ---
while True:
    print("\nAgregar conexión entre ciudades")
    origen = input("Ingrese el nombre del nodo origen: ")
    destino = input("Ingrese el nombre del nodo destino: ")
    distancia = int(input("Ingrese la distancia entre los nodos: "))
    tiempo = int(input("Ingrese el tiempo estimado: "))

    GrafoRutas.agregar_Adyacente(origen, destino, distancia, tiempo)
    print(f"Conexión agregada entre {origen} y {destino}.")

    continuar = input("¿Desea agregar otra conexión? (s/n): ")
    if continuar.lower() != "s":
        break

# --- Mostrar conexiones ---
GrafoRutas.mostrarConexiones()

# --- Búsqueda de ruta ---
print("\nBúsqueda de ruta entre dos ciudades")
origen_busqueda = input("Ingrese el nodo origen: ")
destino_busqueda = input("Ingrese el nodo destino: ")

ruta_encontrada = GrafoRutas.buscar_ruta(origen_busqueda, destino_busqueda)

if ruta_encontrada:
    print(f"Ruta encontrada: {' -> '.join(ruta_encontrada)}")
else:
    print("No existe una ruta entre esas ciudades.")
