#tipos de print/input
#print("Bom dia")
#print("O valor de x é: ")
# x = input("O valor de x é:")
# print (f"O usuario digitou o valor {x}")
import math

#lista de exercicios 1
def exercicio1_ola_mundo():
    print("Executando o exercicio 1...")
    print("EXERCICIOS 1 - coloque ola mundo na tela")
    print("\nOlá Mundo")


def exercicios2_pedir_e_mostrar_n():
    print("Executando o exercicio 2...")
    print("EXERCICIOS 2 - pedir UM NUMERO E MOSTRAr a mensagem com o numero informado")
    Resultado = int(input("\nDigite um numero aleatorio: "))
    print(input(Resultado))
    
def exercicios3_soma_de_2_numeros():
    print("Executando o exercicio 3...")
    print("Exercicio 3 - Pedir dois numeros e imprimir a soma")

    n1 = float(input("\nDigite o primeiro numero: "))
    n2 = float(input("Digite o segundo:"))
    soma = n1 + n2
    print(soma)

def exercicios4_4notas_bimestrais_media():
    print("Executando o exercicio 4...")
    print("Exercicio 4 - pedir 4 notas bimestrais e mostra a média")

    nt1 = float(input("\nDigite sua primeira nota do bimestre: "))
    nt2 = float(input("Digite sua primeira nota do bimestre: "))
    nt3 = float(input("Digite sua primeira nota do bimestre: "))
    nt4 = float(input("Digite sua primeira nota do bimestre: "))

    print("Suas notas são: ", nt1,",", nt2,",", nt3,",", nt4)
    media_das_notas = (nt1 + nt2 + nt3 + nt4)/4
    print("Sua média de acordo com suas 4 provas é: ", media_das_notas)


def exercicios5_metrospara_cm():
    print("Executando o exercicio 5...")
    print("Exercicio 5 - converter metros para centimetros")

    metros = float(input("\nInforme quantos metros deseja converter: "))
    Cm = metros * 100
    print(f"a Conversão de {metros}m é igual a {Cm} cm ")

def exercicio6_areado_circulo():
    print("Executando o exercicio 6...")
    print("Exercicio 6 - Calcular e mostrar a area de um circulo")

    raio = float(input("\nInforme o valor do raio do circulo(em centimetros): "))
    pi = 3.14
    area = pi * raio ** 2
    print(f"A área do circulo com raio {raio} é: {area:.2f}")


def exercicio7_calcular_area_Q_edobro():
    print("Executando o exercicio 7...")
    print("Exercicio 7 - Calcular a área do quadrado e mostrar o dobro")

    lado = float(input("\nInforme o lado do quadrado em Cm: "))
    areaQ = lado + lado
    dobroQ = areaQ * 2
    print(f"o dobro da área do quadrado é: {dobroQ:.2f}")

def exercicio8_calcular_salario_do_mes():
    print("Executando o exercicio 8...")
    print("Exercicio 8 - Calcular o salário do mes")
    horas_trabalhadas = float(input("\nInforme quantas horas trabalhas você tem na semana: "))
    valor_hora = float(input("Informe quanto você ganha por hora: "))
    salario = valor_hora * horas_trabalhadas
    print(f"O salário Mensal é: R$ {salario:.2f}")

def exercicio9_solicitar_altura_epeso_ideal():
    print("Executando o exercicio 9...")
    print("Exercicio 9 - Solicita a altura da pessoa ao usuário")
    #calcula o peso ideal usando a formula fornecida
    altura = float(input("\nInfome sua altura: "))
    genero = input("Informe seu gênero: (M/F)").strip().upper()

    if genero == "M" or "m":
        peso_ideal_M = (72.7 * altura) - 58
        print(f"Seu peso ideal é {peso_ideal_M:.2f} kg")
    elif genero == "F" or "f":
        peso_ideal_F = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é {peso_ideal_F:.2f} kg")
    else:
        print("GENÊRO INVÁLIDO! Digite 'M' para Masculino e 'F' para Feminino. Tente novamente!")

def exercicio10_peso_peixes_regulamento_multa():
    print("Executando o exercicio 10...")
    print("Exercicio 10 - Solicita peso do peixe, verifica se o peixe ultrapassa o limite, e calcula a multa")
    peso_peixes = float(input("\nInforme o peso dos peixes em Quilos: "))
    qual_peixaria = input("Qual peixaria você gostaria de pesar seu(s) peixe(s)? (Peixaria Kotukateucu/Peixaria KevinMama)? ").strip().lower()
    limite1 = 50 #peixaria 1
    limite2 = 40 # peixaria 2
    if qual_peixaria == "peixaria kotukateucu":
        if peso_peixes > limite1:
            excesso1 = peso_peixes - limite1
            multa1 = excesso1 * 4.00 #4 reais cada quilo que passou do limite
            print("\nVocê excedeu o limite de peso de",limite1, "quilos em", excesso1, "quilos")
            print("\nPortanto, você deve pagar uma multa de R$", multa1)
        else:
            print("Você não excedeu o limite de peso de ", limite1, "quilos, não a multa a ser paga!")

    elif qual_peixaria == "peixaria kevinmama":
        if peso_peixes > limite2:
            excesso2 = peso_peixes - limite2
            multa2 = excesso2 * 3.00
            print("\nVocê excedeu o limite de peso de",limite2, "quilos em", excesso2, "quilos")
            print("\nPortanto, você deve pagar uma multa de R$", multa2)
        else:
            print("Você não excedeu o limite de peso de ", limite2, "quilos, não a multa a ser paga!")

    else:
        print("Você não escolheu nenhuma Peixaria seu arrombado, volte e escolha uma das opções!")
    
def exercicio11_sistemafinanceiro():
    print("Executando o exercicio 11...")
    print("Exercicio 11 - Calcula salario bruto, mensal, descontos, liquido")
    #solicita o valor ganho por hora e o numero de horas trabalhas no mes
    valor_ganho_por_hora = float(input("\n Digite o quanto você ganha por hora: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

    #calcular salario bruto
    salario_bruto = valor_ganho_por_hora * horas_trabalhadas
    #calcula os descontos
    imposto_renda = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05

    #Salario liquido
    salario_liquido = salario_bruto - imposto_renda - inss - sindicato

    #Resultados
    print("+ Salário Bruto : R$", salario_bruto)
    print(" - IR (11%) : R$", imposto_renda)
    print("- INSS (8%) : R$", inss)
    print("- Sindicato (5%) : R$", sindicato)
    print("= Salário Líquido : R$", salario_liquido)

def exercicio12_temperaturas():
    print("Executando o exercicio 12...")
    print("Exercicio 12 - Convertor de temperaturas")

    qual_temp = input("\nQual temperatura você quer converter?Digite apenas a Inicial (Fahrenheit / Celsius)? ").strip().lower()
    if qual_temp == "f":
        temperatura_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        conversao_celsius = (5*temperatura_fahrenheit - 32)/9
        print(f"A temperatura em Celsius é: {conversao_celsius:.2f}")
    elif qual_temp == "c":
        temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
        conversao_fahrenheit = (1.8*temperatura_celsius + 32)
        print(f"A temperatura em Fahrenheit é: {conversao_fahrenheit:.2f}")

def sair():
    print("Saindo do Programa...")
    exit()

#criar menu dicionario
menu = {
    "1":("Exercicio 1 - Olá Mundo!", exercicio1_ola_mundo) ,
    "2": ("Exercicio 2 - Pedir e mostrar um número!", exercicios2_pedir_e_mostrar_n),
    "3": ("Exercicio 3 - Some 2 números!", exercicios3_soma_de_2_numeros),
    "4": ("Exercicio 4 - Calcular a média de 4 notas!", exercicios4_4notas_bimestrais_media),
    "5": ("Exercicio 5 - Convertor de Metros para Cm!", exercicios5_metrospara_cm),
    "6": ("Exercicio 6 - Calcular a area do Circulo!", exercicio6_areado_circulo),
    "7": ("Exercicio 7 - Calcular a área de um quadrado e o dobro dela!", exercicio7_calcular_area_Q_edobro),
    "8": ("Exercicio 8 - Calcular o Salário do Mês!", exercicio8_calcular_salario_do_mes),
    "9": ("Exercicio 9 - Descubra qual o seu peso ideal pela sua Altura!", exercicio9_solicitar_altura_epeso_ideal),
    "10":("Exercicio 10 - Peso dos peixes e regulamento das peixarias!", exercicio10_peso_peixes_regulamento_multa),
    "11":("Exercicio 11 - Descubra todo seu salário com os descontos KKKKK!", exercicio11_sistemafinanceiro),
    "12":("Exercicio 12 - Conversor de temperaturas C e F!", exercicio12_temperaturas),
}

#Loop do menu interativo
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