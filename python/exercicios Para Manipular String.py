#1 receba uma string digitado pelo usuário
#2 verrifica quais vogais estão presentes na string dada
#3 conta quantas ocorrencias de cada vogal estao presentes na string, independente de ser maiuscula ou minuscula
# 4 imprima uma palavra com tanto maiusculas tanto minusculas

def exercicio1():
    palavra = input("Digite qualquer palavra (Pode usar MAIUCULAS e minusculas juntas): ")
    vogais = "aeiou"
    ocorrencias_vogais = {}
    vogais_unicas_encontradas = set()

    for letra in palavra.lower():
        if letra in vogais:
            vogais_unicas_encontradas.add(letra)
            ocorrencias_vogais[letra] = ocorrencias_vogais.get(letra, 0) + 1

    print(f"Palavra digitada: {palavra}")
    print("Vogais presentes na palavra:", ", ".join(sorted(vogais_unicas_encontradas)))
    print("Ocorrências de cada vogal:")
    for vogal, count in ocorrencias_vogais.items():
        print(f"'{vogal}': {count}")
        

def exercicio1simples():
    palavra = input("Digite qualquer palavra (Pode usar MAIUCULAS e minusculas juntas): ")
    palavra_maiuscula = palavra.upper()

    a = palavra_maiuscula.count("A")
    e = palavra_maiuscula.count("E")
    i = palavra_maiuscula.count("I")
    o = palavra_maiuscula.count("O")
    u = palavra_maiuscula.count("U")

    print("{} possui:".format(palavra))
    if a > 0:
        print("\tVogal a: {}".format(a))
    if e > 0:
        print("\tVogal e: {}".format(e))
    if i > 0:
        print("\tVogal i: {}".format(i))
    if o > 0:
        print("\tVogal o: {}".format(o))
    if u > 0:
        print("\tVogal u: {}".format(u))

def exercicio2():
    print("O preço base do Museu é R$10,00") 
    preco_base = float(10)
    #menor que 5 anos não paga
    #crianças entre 5 e 12 anos meia entrada
    # Adolecentes de 13 e 17 anos tem 20% de desconto
    # Adultos entre 18 e 70 anos pagam o valor base
    #Maiores de 70 anos nao pagam
    idade = int(input("Qual a idade do visitante? "))  
    
    if 0 < idade < 5:
        print("O Visitante não paga")
    elif 5 < idade <= 12:
       novo_preco =  preco_base/2
       print(f"O visitante pagará {novo_preco:.2f}")
    elif 13 <= idade <= 17:
        desconto = preco_base * 0.2 #20%
        novo_preco = preco_base - desconto
        print(f"O preço que o visitante irá pagar é de {novo_preco}")
    elif 18 <= idade <= 69:
        print(f"Paga o valor base {preco_base}")
    elif 70 < idade <= 130: 
        print("O visitante não paga")
    else:
        (print("idade invalida! Tente novamente"))
    
   
#criar menu dicionario
menu = {
    "1.1":("Exercicio 1.1 - contador de vogais cod melhor", exercicio1) ,
    "1": ("Exercicio 1 - contador de vogais", exercicio1simples),
    "2": ("Exercicio 2 - preco do museu", exercicio2)
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