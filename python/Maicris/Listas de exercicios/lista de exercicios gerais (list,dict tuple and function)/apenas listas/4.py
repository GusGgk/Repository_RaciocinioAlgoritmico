"""Peça uma lista de palavras e exiba todas as palavras na ordem inversa"""

lista = []

while True:
    palavra = input("Digite uma palavra para ser invertida(0 para sair): ")
    if palavra == "0":
        break
    lista.append(palavra)

print(lista)

invertidas = []
for palavra in lista:
    invertidas.append(palavra[::-1])

print(invertidas)