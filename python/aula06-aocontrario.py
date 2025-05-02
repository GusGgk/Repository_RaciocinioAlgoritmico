def exercicio1():
    #imprimir os numeros pares de 1 a 20 utilizando um laço de repetição while
    for numero in range (0, 21, 2):
        print(numero)
    
    
def exercicio2():
    # usando while faça soma de todos os numeros de 1 a 100 
    acc = 1
    soma = 0
    while acc <= 100:
        soma = soma + acc
        print(acc)

def exercicio3():
    #usando for de 1 a 10, cada um elevado ao quadrado
    for numero in range(1, 11):
        quadrado = numero ** 2
        print(f"O quadrado de {numero} é {quadrado}")
    

def exercicio4():
    #Escreva um programa de 100 a 1 em ordem decrescente utilizando um laço de repetição while
    n = 100
    while n > 1:
        print(n)
        n -= 1
    
       

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
    for numero in range(0, 51, 5):
        print(numero)

menu = {
    "1":("Exercicio 1 - numeros pares ate o 20", exercicio1) ,
    "2": ("Exercicio 2 - soma de 1 a 100", exercicio2),
    "3": ("Exercicio 3 - quadrado dos numeros ", exercicio3),
    "4": ("Exercicio 4 - 100 ao 1 decrescente ", exercicio4),
    "5": ("Exercicio 5 - fatorial ", exercicio5),
    "6": ("Exercicio 6 - pulando de 5 em 5", exercicio6)
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