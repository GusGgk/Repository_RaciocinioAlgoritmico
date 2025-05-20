"""
Criar um programa que efetua a soma de duas matrizes 3x3, sabendo
que a soma das matrizes 3x3 é uma nova matriz 3x3 onde cada elemento
é resultado da soma dos elementos das matrizes na mesma posição.
Exemplo:
[1 2 3    
 4 5 6
 7 8 9]
+
[3 2 3
 1 3 3
0 2 2]


"""
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [3, 2, 3],
    [1, 3, 3],
    [0, 2, 2]
]

'''
for i in range(3):
    linha = []
    for j in range(3):
        soma = m1[i][j] + m2[i][j]
        linha.append(soma)
    print(linha)
'''
resultado = []
for i in range(3):
    linha = []
    for j in range(3):
        soma = m1[i][j] + m2[i][j]
        linha.append(soma)
    resultado.append(linha)
for linha in resultado:
    print(linha)
