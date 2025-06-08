def fatorial(n):
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
    return resultado

numero = int(input("Informe um numero para fatoração: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")
    
