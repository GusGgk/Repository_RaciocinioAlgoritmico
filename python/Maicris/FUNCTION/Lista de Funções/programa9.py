"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127
-> 721"""

def reverter():
    n = int(input("Informe um número para ser invertido: "))
    numero = str(n)
    invertido = int(numero[::-1])
    return invertido

print(reverter())