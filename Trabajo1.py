import random

def generar_mazo():
    "Genera un mazo de 52 cartas de poker desordenado"
    palos = ["c", "t" ,"d","p"]
    valores = list(range(1,14))

    mazo = []
    for palo in palos:
        for valor in valores:
            mazo.append(f"{valor}{palo}")

    random.shuffle(mazo)
    return mazo

#Generar mazo y mostrar el mazo
mazo_desordenado = generar_mazo()
#print(mazo_desordenado)
#print(f"\nNumero de cartas en el mazo:{len(mazo_desordenado)}")
def separarCartas():
    Lista_separar =[]
    for carta in mazo_desordenado:
        #Toma todo menos el ultimo y el otro toma solo el ultimo caracter
        Separacion= int(carta[:-1]),carta[-1]
        Lista_separar.append(Separacion)

    return Lista_separar

Lista_separada= separarCartas()

def bubble_sort(lista):
    n = len(lista)
    print(n)
    # Recorre toda la lista
    for i in range(n):
        # El bucle interno se detiene antes del último elemento ya ordenado
        for j in range(0, n-i-1):
            # Compara elementos adyacentes
            if lista[j] > lista[j+1]:
                # Intercambia los elementos si están en el orden incorrecto
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

Lista_ordenada = bubble_sort(Lista_separada)
#print(Lista_ordenada)

def Agrupar(lista):
    Corazones = []
    Picas = []
    Diamantes = []
    Treboles=[]

    for numero,letra in lista:
            if letra == "c":
                Corazones.append((numero,letra))
            elif letra =="p":
                Picas.append((numero,letra))
            elif letra == "d":
                Diamantes.append((numero,letra))
            else:
                Treboles.append((numero,letra))
    return Corazones,Picas,Diamantes,Treboles

Lista_Final = Agrupar(Lista_ordenada)
#print(Lista_Final)
Corazones, Picas, Diamantes, Treboles = Agrupar(Lista_ordenada)
ListaDefinitiva = Corazones + Picas + Diamantes + Treboles
#print("Corazones:", Corazones)
#print("Picas:", Picas)
#print("Diamantes:", Diamantes)
#print("Tréboles:", Treboles)
print("La lista ordenada:", ListaDefinitiva)
