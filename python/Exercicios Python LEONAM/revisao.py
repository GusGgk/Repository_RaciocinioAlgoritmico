#escreva um programa que calcule o fatorial de um numero inserido pelo usuario utilizando um laço de repetição while
num = int(input("Digite um numero : "))
resultado = 1
i = 1
while i <= num:
    resultado *= i
    i += 1
print("O fatorial de",num, "é:", resultado)