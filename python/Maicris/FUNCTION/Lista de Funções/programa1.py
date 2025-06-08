"""ENUNCIADO
1. Faça um programa para imprimir:
1
2 2
3 3 3
.....
n n n n n n ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima
linha."""

def receber_numero():
    while True:
        n = int(input("Digite algum número para repetir: "))
        if n > 0:
            return n

def imprimir_numero(n):
    for i in range(1, n + 1):
        print(f"{i} " * i)
        
n = receber_numero()
imprimir_numero(n)