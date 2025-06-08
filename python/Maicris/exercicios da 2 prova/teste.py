def somar(*numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
    return soma

resultado = somar(2,4,5,6,7,8,5,3,32,2)
print(resultado)