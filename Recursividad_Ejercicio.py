def Recursiva(n):
    if n <10:
        return n
    elif n>=10:
        return (n % 10) + Recursiva(n // 10)



print (Recursiva(122))