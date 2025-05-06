#LISTA EXTRA DE EXERCICIOS

import math

def exercicio3_VERSAO3 ():

    a = 7
    h = 63 / a  # Calculando h a partir da área
    d = (a**2 + h**2) ** 0.5  # Calculando a raiz quadrada

    print(f"A diagonal do retângulo é aproximadamente: {d:.2f}")

def exercicio5():
    # Solicita os coeficientes ao usuário
    a = float(input("Informe o coeficiente a: "))
    b = float(input("Informe o coeficiente b: "))
    c = float(input("Informe o coeficiente c: "))

# Verifica se a equação é de segundo grau
    if a == 0:
        print("O coeficiente 'a' deve ser diferente de zero para uma equação de segundo grau.")
    else:
        # Calcula o discriminante (delta)
        delta = b**2 - 4*a*c

        # Verifica a natureza das raízes com base no delta
        if delta < 0:
            print("A equação não possui raízes reais.")
        elif delta == 0:
            x = -b / (2*a)
            print(f"A equação possui uma raiz real: x = {x:.2f}")
        else:
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            print(f"A equação possui duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}")

def exercicio1():
    pi = 3.1415
    print(pi)

def exercicio2():
    r = float(input("\nDigite qual raio é a do circulo: "))
    pi = 3.14
    perimetro = 2 * pi * r
    print(f"\n O perimetro do circulo é:{perimetro:.2f} ")

def exercicio4():
    r = float(input("\nDigite qual raio é a do circulo: "))
    pi = 3.14
    area_circulo = pi * r**2
    #area_circulo = pi * (r*r)
    print(f"\n A Area do circulo é:{area_circulo:.2f} ")

def exercicio6():
    frase = "Leonam lindo"
    print(frase)

def exercicio7():
    nome = "Power"
    sobrenome = "Guido"
    print(nome, sobrenome)
    nome_completo = nome + " " + sobrenome
    print(nome_completo)

def exercicio8():
    etiqueta = "Etiqueta 1"
    print((etiqueta + " | ") * 20)

def exercicio9():
    nome = input("Digite seu Nome: ")
    sobrenome = input("Digite seu Sobrenome: ")
    print(nome, sobrenome)
    print(f"Bom Dia, {nome}{sobrenome}!")

def exercicio10():
    idade = int(input("Digite sua idade: "))
    print(idade)

def exercicio11():
    pi = float(input("Digite o valor de PI: "))
    print(pi)

menu = {
    "1":("Exercício 01 - PI com 4 casas", exercicio1),
    "2":("Exercício 02 - perimetro do circulo", exercicio2),
    "3":("Exercício 03 - a diagonal do retângulo", exercicio3_VERSAO3),
    "4":("Exercício 04 - Area do circulo", exercicio4),
    "5":("Exercício 05 - Baskara", exercicio5),
    "6":("Exercício 06 - Nome", exercicio6),
    "7":("Exercício 07 - nome e sobrenome", exercicio7),
    "8":("Exercício 08 - etiqueta 1", exercicio8),
    "9":("Exercício 09 - digite seu nome e sobrenome", exercicio9),
    "10":("Exercício 10 - digite sua idade", exercicio10),
    "11":("Exercício 11 - digite o valor de PI", exercicio11),
}

#menu loop
while True:
    print("\n===== MENU =====")
    for chave, (nome_exercicio,funcao) in menu.items():
        print(f"{chave} - Exercício {nome_exercicio}")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        print("Saindo do programa... Até mais!")
        break
    elif opcao in menu:
        nome_exercicio, funcao = menu[opcao]
        funcao()  # Executa a função correspondente
    else:
        print("Opção inválida! Tente novamente.\n")
