"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
numeros = []
for i in range(5):
    n = int(input(f"Informe o {i+1}° numero: "))
    numeros.append(n)

print(numeros)

#help("__main__")