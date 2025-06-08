"""ENUNCIADO
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três
argumentos """
numeros = []

for i in range(3):
    n = int(input(f"Digite o {i+1}º numero: "))
    numeros.append(n)
    
def somar(a, b, c):
    soma = a + b + c
    return soma

soma = somar(*numeros)
print(soma)