"""ENUNCIADO
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
elementos do vetor
"""
A = []
for i in range(10):
    num = int(input(f"Digite o {i+1} número: "))
    A.append(num)
print(A)

soma_dos_quadrados = 0
for i in A:
   quadrado = i ** 2
   soma_dos_quadrados += quadrado
   print(quadrado)
print(f"A soma dos quadrados dos elementos de A é: {soma_dos_quadrados}")



#help("__main__")