"""criar uma função que converta lista em dicionario"""

lista = []
def listInDict():
    d = {}
    for i in range(len(lista)):
        d[i+1] = lista[i]
    return d

while True:
    num = int(input("Digite um numero para lista: "))
    if num == 0:
        print(listInDict())
        break
    lista.append(num)