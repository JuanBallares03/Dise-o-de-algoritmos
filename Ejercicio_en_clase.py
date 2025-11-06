class Furgoneta():

    def __init__(self, marca, modelo, capacidad_carga, rutas, horas_disponibles,capacidad_actual):
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

    def agregar_Adyacente(self, origen, destino, distancia, tiempo):
        # Verificamos que ambos nodos existan
        if origen in self.nodos and destino in self.nodos:
            # Añadimos el nodo destino a la lista de adyacentes del nodo origen
            self.nodos[origen].Adyacentes.append({
                "destino": destino,
                "distancia": distancia,
                "tiempo": tiempo
            })
        else:
            print("Uno o ambos nodos no existen en el grafo.")
    def mostrarConexiones():
        pass

#Creamos los objetos Furgoneta
Furgoneta1 = Furgoneta("Mazda", "BT-50", 1000, ["Ruta1", "Ruta2"], 8, 100)
Furgoneta2 = Furgoneta("Toyota", "Hilux", 900, ["Ruta3", "Ruta4"], 8, 200)
Furgoneta3 = Furgoneta("Ford", "Ranger", 1100, ["Ruta5", "Ruta6"], 8, 300)
Furgoneta4 = Furgoneta("Nissan", "Navara", 950, ["Ruta7", "Ruta8"], 8, 400)
Furgoneta5 = Furgoneta("Chevrolet", "S10", 1050, ["Ruta9", "Ruta10"], 8, 500)

#Inicializamos el grafo y agregamos un nodo
GrafoRutas = Grafo()
nombre_nodo = input("Ingrese el nombre del nodo: ")
GrafoRutas.agregar_nodo(nombre_nodo)
nodo_obtenido = GrafoRutas.nodos[nombre_nodo]

GrafoRutas.agregar_Adyacente("Bogota","Medellin",10,5)
print(f"Nodo agregado: {nodo_obtenido.nombre}")


