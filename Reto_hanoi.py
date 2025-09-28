A = [3, 2, 1]  # Puedes cambiar el número de discos
B = []
C = []

def Hanoi(n, origen, destino, auxiliar):
    if n == 1:
        destino.append(origen.pop())
        print(f"Mover disco a {destino}")  # Para ver los movimientos
    else:
        Hanoi(n-1, origen, auxiliar, destino)  # Paso 1
        destino.append(origen.pop())           # Paso 2
        print(f"Mover disco a {destino}")
        Hanoi(n-1, auxiliar, destino, origen)  # Paso 3

# Llamada inicial
Hanoi(len(A), A, C, B)

# Mostrar resultado final
print("A:", A)
print("B:", B)
print("C:", C)