"""ENUNCIADO
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
consoantes.
"""
caracteres = []
consoantes = []
vogais = "aeiou"
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for i in range(10):
    caracter = input(f"Digite o {i+1} caractere: ")
    caracteres.append(caracter.lower())

print(f"Os caracteres digitados foram: {caracteres}" )

for caracter in caracteres:
    if caracter in alfabeto and caracter not in vogais:
        consoantes.append(caracter)

print(f"Foram lidas", len(consoantes), f"consoantes: {consoantes}")

#help("__main__")