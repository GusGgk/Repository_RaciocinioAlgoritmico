"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere 'P', se
seu argumento for positivo, e 'N', se seu argumento for zero ou negativo."""

def verificar_sinal(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'
  
  
valor = int(input("Digite o valor: "))
resultado = verificar_sinal(valor)
print(f"Resultado: {resultado}")