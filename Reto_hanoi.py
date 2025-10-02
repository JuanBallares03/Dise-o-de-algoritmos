A = [3, 2, 1]  # Torre inicial (3 discos)
B = []
C = []

def mover(origen, destino, nombre_origen, nombre_destino):
    if origen and (not destino or origen[-1] < destino[-1]):
        destino.append(origen.pop())
        print(f"Mover disco de {nombre_origen} a {nombre_destino}")
    elif destino and (not origen or destino[-1] < origen[-1]):
        origen.append(destino.pop())
        print(f"Mover disco de {nombre_destino} a {nombre_origen}")

def hanoi_iterativo(n, A, B, C):
    # Si n es par, intercambiamos destino y auxiliar
    if n % 2 == 0:
        destino, auxiliar = B, C
        nombre_destino, nombre_auxiliar = "B", "C"
    else:
        destino, auxiliar = C, B
        nombre_destino, nombre_auxiliar = "C", "B"

    origen, nombre_origen = A, "A"

    total_movimientos = (2 ** n) - 1

    for i in range(1, total_movimientos + 1):
        if i % 3 == 1:
            mover(origen, destino, nombre_origen, nombre_destino)
        elif i % 3 == 2:
            mover(origen, auxiliar, nombre_origen, nombre_auxiliar)
        elif i % 3 == 0:
            mover(auxiliar, destino, nombre_auxiliar, nombre_destino)

# Ejecutar
hanoi_iterativo(len(A), A, B, C)

print("\nEstado final:")
print("A:", A)
print("B:", B)
print("C:", C)