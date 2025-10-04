origen = [3, 2, 1]
auxiliar = []
destino = []
def Hanoi(n, origen,auxiliar, destino):
    if n == 1:
        destino.append(origen.pop())
    elif n>1:
        Hanoi(n-1,origen,destino,auxiliar)
        destino.append(origen.pop())
        Hanoi(n-1,auxiliar, origen, destino)


Hanoi(3, origen, auxiliar, destino)
print("Torre final:", destino)

