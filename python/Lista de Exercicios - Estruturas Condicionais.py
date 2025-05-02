#Lista de Exercicios - Estruturas Condicionais

#1
def exercicio1():
    print("Executando o exercicio 1...")
    print("Exercicio 1 - media e materia do aluno")

    matematica = ("matemática").strip().lower()
    portugues = ("português").strip().lower()
    quimica = ("química").strip().lower()
    fisica = ("física").strip().lower()

    materia = input("\nDigite qual matéria você quer saber a nota do aluno: (matemática, português, química, física): ")
    n1 = float(input("\nDigite a primeira nota do aluno: "))
    n2 = float(input("\nDigite a segunda nota do aluno: "))
    n3 = float(input("\nDigite a terceira nota do aluno: "))
    media = n1 + n2 + n3 /3 
    if materia == matematica:
       if media > 6.0:
           print("Você passou em Matemática! ")
       else:
           print("Você reprovou em matemática!")
    elif materia == portugues:
       if media > 6.0:
           print("Você passou em português! ")
       else:
           print("Você reprovou em português!")
    elif materia == quimica:
       if media > 6.0:
           print("Você passou em química! ")
       else:
           print("Você reprovou em química!")
    elif materia == fisica:
       if media > 6.0:
           print("Você passou em física! ")
       else:
           print("Você reprovou em física!")
    else:
        print("Informe alguma matéria")

def exercicio2():
    print("Executando o exercicio 2...")
    print("Exercicio 2 - positivo, negativo ou neutro")

    info = float(input("Informe o número que voce deseja verificar (negativo/positivo/0): "))
    if info < 0:
        print("Seu número é negativo")
    elif info > 0:
        print("Seu número é positivo")
    elif info == 0:
        print("Seu número é zero")
    else:
        print("Invalido")

def exercicio3():
    print("Executando o exercicio 3...")
    print("Exercicio 3 - Consoante ou vogal")
    letra = input("Digite uma letra: ")

   
    letras = letra.strip().lower()

    
    if len(letras) == 1 and letras.isalpha():
        if letras in "aeiou":
            print(f"A letra '{letra}' é uma vogal.")
        else:
            print(f"A letra '{letra}' é uma consoante.")
    else:
        print("Entrada inválida. Por favor, digite apenas uma letra.")

def exercicio4():
    print("Executando o exercicio 4...")
    print("Exercicio 4 - qual triangulo voce escolheu?")
    t1 = float(input("Informe o primeiro do triângulo: ")) 
    t2 = float(input("Informe o segundo lado do triângulo: ")) 
    t3 = float(input("Informe o terceiro triângulo: ")) 

    
    if t1 == t2 == t3:
        print("\nO triângulo é Equilatero pois todos os jogos são iguais")
    elif t1 == t2 or t1 == t3 or t2 == t3:
       if t1 == t2:
            print(f"\nO triângulo é isósceles pois os lados {t1:.2f} e {t2:.2f} são iguais.")
       elif t1 == t3:
            print(f"\nO triângulo é isósceles pois os lados {t1:.2f} e {t3:.2f} são iguais.")
       elif t2 == t3:
            print(f"\nO triângulo é isósceles pois os lados {t2:.2f} e {t3:.2f} são iguais.")
    else:
        print("\nO Triângulo é escaleno,pois todos os lados são diferentes")

def exercicio5():
    print("Executando o exercicio 5...")
    print("Exercicio 5 - seu salario e sua bonificação")
    salario = float(input("Informe seu salário: "))   
    tempo_na_empresa = float(input("Informe a quanto anos você está na empresa: "))
    restante = 5 
    tempo = restante - tempo_na_empresa
    
    if tempo_na_empresa > 5:
        bonus = salario * 0.05 #5% do salario
        novo_salario = salario + bonus
        print(f"\nParabéns você ganhou um bônus de:{bonus:.2f} ")
        print(f"\nSeu salário com o bônus agora é:{novo_salario:.2f} ")
    else:
        print(f"\nSeu salário atual é {salario:.2f}, você ainda não bateu a meta para o bônus, falta {tempo} para vocÊ conseguir!")

def exercicio6():
    print("Executando o exercicio 6...")
    print("Exercicio 6 - Desconto de Produto")
    
    preco = float(input("Informe o preço somado dos produtos comprados: "))
    if (preco > 100 and preco < 1000):
        desconto = preco * 0.10 # 10% do preco do produto
        novo_preco = preco - desconto
        print(f"\nSeu produto custava {preco} e com o desconto de {desconto} agora sua compra deu {novo_preco}")
    elif (preco > 1000):
        desconto = preco * 0.20 # 20% do preco do produto
        novo_preco = preco - desconto
        print(f"\nSeu produto custava {preco} e com o desconto de {desconto} agora sua compra deu {novo_preco:.2f}")
    else:
        falta_valor = 100 - preco
        print(f"\nVocê não terá nenhum desconto, compre mais {falta_valor:.2f} para ganhar um desconto de 10%.")

def exercicio7():
    print("Executando o exercicio 7...")
    print("Exercicio 7 - Faixa etária")
    info_idade = int(input("Informe a idade da pessoa desejada: "))
    if 0 < info_idade <= 12:
        print("essa pessoa é criança")
    elif 12 < info_idade <= 17:
        print("Essa pessoa é adolecente")
    elif 17 < info_idade <= 59:
        print("Essa pessoa é adulta")
    elif 59 < info_idade <= 120:
        print("Essa pessoa é idosa")
    else:
        print("Então ela ta morta KKKKKKKKKKKKKK") 
        
def exercicio8():
    print("Executando o exercicio 8...")
    print("Exercicio 8 - Classificação de nota")
    nota = float(input("Informe a sua nota: "))
    if 9 < nota <= 10:
        print(f"\n a classificação da sua nota {nota} é A")
    elif 7 < nota <= 8.9:
        print(f"\n a classificação da sua nota {nota} é B")
    elif 5 < nota <= 6.9:
        print(f"\n a classificação da sua nota {nota} é C")
    elif 0 <= nota <= 5:
        print(f"\n a classificação da sua nota {nota} é D")
    else:
        print("Informe uma nota de 0 a 10...")

def exercicio9():
    print("Executando o exercicio 9...")
    print("Exercicio 9 - Salário e aliquota")
    salario_anual = float(input("Informe o seu salário anual: "))
    if 0 < salario_anual <= 20000:
        aliquota = 0
        print(f"\nSeu salário é de {salario_anual} e sua aliquota é de {aliquota}%")
    elif 20001 < salario_anual <= 50000:
        aliquota = 0.15
        calculo_aliquota = salario_anual * aliquota
        novo_salario = salario_anual - calculo_aliquota
        print(f"\nSeu salário é de {salario_anual} e por conta de sua aliquota seu novo salario é de {novo_salario:.2f}")
    elif 50001 < salario_anual:
        aliquota = 0.25
        calculo_aliquota = salario_anual * aliquota
        novo_salario = salario_anual - calculo_aliquota
        print(f"\nSeu salário é de {salario_anual} e por conta de sua aliquota seu novo salario é de {novo_salario:.2f}")
    else:
        print("\nsuas informações estão incorretas, informe um salário!")
   
   
def exercicio10():
    print("Executando o exercicio 10...")
    print("Exercicio 10 - Cnh, idades se posso tirar carteira")
    cnh = int(input("Digite sua idade: "))
    if 0 < cnh <= 17 or 18 <= cnh <= 20:
        if 0 < cnh <= 17:
            print("\nVocê é menor de idade e não pode tirar carteira")
        elif 18 < cnh <= 20:
            print("\nVocê é maior de idade mas ainda não pode tirar carteira")
    else:
        print("\nVocÊ está apto a tirar carteira pois já é maior de 21 anos")
         
    
        


menu = {
    "1":("Exercício 01 - media e materia do aluno", exercicio1),
    "2":("Exercício 02 - positivo,negativo ou 0", exercicio2),
    "3":("Exercício 03 - consuante ou vogal", exercicio3),
    "4":("Exercício 04 - Triângulo: Isosceles,equilatero ou escaleno", exercicio4),
    "5":("Exercício 05 - Salário e bonificação", exercicio5),
    "6":("Exercício 06 - Desconto de produto", exercicio6),
    "7":("Exercício 07 - Qual faixa etaria a pessoa está", exercicio7),
    "8":("Exercício 08 - Classificação de nota", exercicio8),
    "9":("Exercício 09 - Salário e sua aliquota", exercicio9),
    "10":("Exercício 10 - CNH", exercicio10),
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
