def exercicio1():
    #imprimir os numeros pares de 1 a 20 utilizando um laço de repetição while
    numero = 0
    while numero <= 20:
        print(numero)
        numero += 2
        
    
    
def exercicio2():
    # usando for e range  faça soma de todos os numeros de 1 a 100 
    acc = 0
    for i in range(1, 101):
        acc += i
    print(acc)

def exercicio3():
    #calcular o quadrado do 1 ao 10
    numero = 1
    while numero <= 10:
        quadrado = numero ** 2  # Calcula o quadrado do número
        print(f"O quadrado de {numero} é: {quadrado}")
        numero += 1  # Incrementa o número para a próxima iteração

def exercicio4():
    #Escreva um programa de 100 a 1 em ordem decrescente utilizando um laço de repetição for e a função range
    for i in range(100, 0, -1):
        print(i)

def exercicio5():
    #faça um programa que calcule o fatorial de um numero inserido pelo usuario utilizando o while
    i = int(input("Digite algum numero inteiro para calcular o fatorial: "))
    i_original = i
    fatorial = 1
    while i > 1:
        fatorial = fatorial * i
        i = i - 1 # decrementar variavel
    print(f"O fatorial de {i_original} é: {fatorial}")

def exercicio6():
    #escreva um programa que imprima numero de 1 a 50 usando for e range pulando de 5 em 5
   for i in range(0, 51, 5):
       print(i)
        
def exercicio7():
    #Escreva um programa que solicite ao usuario um numero e imprima a tabuada desse numero de 1 a 10, utilizando o for
   numero = int(input(" Digite um numero para calcular sua tabuada: "))
   numero_original = numero
   print(f"Tabuada do numero {numero_original}: ")
   for i in range(1,11):
       resultado = numero_original * i
       print(f"{numero_original} x {i} = {resultado}")
       
def exercicio8():
    #Escreva um programa que calcule a media de 5 numeros inseridos pelo usuario, usando um laço de repetição while
    soma = 0
    i = 0
    quantidade = 5

    while i < quantidade:
        numero = float(input(f"Digite o {i + 1}º número: "))
        soma += numero
        i += 1

    media = soma / quantidade
    print(f"A média dos {quantidade} números é: {media}")
        
    #EXERCICIO 9
    

menu = {
    "1":("Exercicio 1 - numeros pares ate o 20", exercicio1) ,
    "2": ("Exercicio 2 - soma de 1 a 100", exercicio2),
    "3": ("Exercicio 3 - quadrado dos numeros ", exercicio3),
    "4": ("Exercicio 4 - 100 ao 1 decrescente ", exercicio4),
    "5": ("Exercicio 5 - fatorial ", exercicio5),
    "6": ("Exercicio 6 - pulando de 5 em 5", exercicio6),
    "7": ("Exercicio 7 - multiplicação ate o 10 de um numero", exercicio7),
    "8": ("Exercicio 8 - media de 5 numeros", exercicio8)
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