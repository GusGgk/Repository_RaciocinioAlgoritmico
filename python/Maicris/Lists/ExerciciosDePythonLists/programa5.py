"""A matriz identidade é uma matriz de mesma quantidade de linhas e
colunas que tem todos os elementos da diagonal principal (de cima para
baixo, esquerda para direita) iguais a 1, e demais elementos iguais a 0.
Criar um programa que solicita o tamanho da matriz desejada, que gera a
matriz identidade.
"""
matriz_desejada = int(input("Importe a quantidade de matriz desejada(Exemplo: se quer uma matriz de 5x5 digite 5): "))

matriz = []

for i in range(matriz_desejada):
    linha = []
    for j in range(matriz_desejada):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
for linha in matriz:
    print(linha)