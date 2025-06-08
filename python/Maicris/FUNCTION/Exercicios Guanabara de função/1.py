"""Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular(largura e comprimento)
e mostre a área do terreno."""

def area(l, c):

    area_terreno = l*c
    return area_terreno
    

print("Controle do Terreno")
print("-------------------")


largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))

print(f"A área de um terreno {largura}x{comprimento} é de {area(largura,comprimento)}m²")