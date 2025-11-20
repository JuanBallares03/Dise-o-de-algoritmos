def contar_formas_escalera(N):
    
    if N < 0:
        print("El número de escalones no puede ser negativo.")
        return None
    if N == 0:
        return 1
    if N == 1:
        return 1
    if N == 2:
        return 2
    
    dp = [0] * (N + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[N]

try:
    NumeroEscaleras= int(input("Digite socio:"))
    print(contar_formas_escalera(NumeroEscaleras))
except ValueError:
    print("Por favor, ingrese un número entero válido.")