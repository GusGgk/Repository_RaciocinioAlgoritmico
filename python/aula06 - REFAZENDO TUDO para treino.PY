#REFAZENDO TODOS OS EXERCICIOS FEITOS DA LISTA DE HOJE 08/04

#exercicio 1 - CHECK ⭐
#imprimir os numeros pares de 1 a 20 utilizando um laço de repetição while
#numero = 0
#while numero <= 20:
#    print(numero)
#    numero += 2


#exercicio 2 ⭐
# usando for e range  faça soma de todos os numeros de 1 a 100 
#s = 0
#for i in range(1,101):
#    s += i
#print(s)

#exercicio 3 ⭐
#calcular o quadrado do 1 ao 10 while
#numero = 1
#while numero <= 10:
#    quadrado = numero ** 2
#    print(f"O {numero} tem seu resultado de quadrado = à {quadrado}")
#    numero += 1

#exercicio 4 ⭐
#Escreva um programa de 100 a 1 em ordem decrescente utilizando um laço de repetição for e a função range
#for i in range(100, 0, -1):
#    print(i)

#exercicio 5 ⭐💔 foi mais ou menos
#faça um programa que calcule o fatorial de um numero inserido pelo usuario utilizando o while
#numero = int(input("Digite o numero que deseja saber seu fatoral: "))
#numero_original = numero
#fatorial = 1
#while numero > 1:
#    fatorial = fatorial * numero
#    numero = numero - 1
#print(f"O numero {numero_original} tem seu fatorial no resultado de {fatorial}")

#exercicio 6 ⭐
#escreva um programa que imprima numero de 1 a 50 usando for e range pulando de 5 em 5
#for i in range(0,51,5):
#    print(i)

#exercicio 7⭐ quase 100% sem ajuda
 #Escreva um programa que solicite ao usuario um numero e imprima a tabuada desse numero de 1 a 10, utilizando o for
#numero = int(input("Digite um numero para calcular sua tabuada: "))
#numero_original = numero
#print(f"Tabuada do numero {numero_original}:")
#for i in range(1, 11):
#    resultado = numero * i
#    print(f"{numero_original} x {i} = {resultado}.")


#exercicio 8 ⭐💔 tive muita dificuldade
#Escreva um programa que calcule a media de 5 numeros inseridos pelo usuario, usando um laço de repetição while
#soma = 0
#i = 0
#quantidade = 5
#while i < quantidade:
#    numero = float(input(f"Digite o {i + 1}º Numero: "))
#    soma += numero
#    i+=1
    
#    media = soma / quantidade
#print(f"A média dos {quantidade} numeros é de: {media}")

#EXERCICIOS AO CONTRARIO - EXERCICIOS QUE USEI FOR  USO WHILE E VICE VERSA
#EXERCICIO 1 ⭐
# imprimir os numeros pares de 1 a 20 utilizando for

#for i in range(0,21,2):
#    print(i)

#exercicio 2 💔⭐💔 ajuda da IA porem estava quase
# usando while  faça soma de todos os numeros de 1 a 100 
#acc = 1
#soma = 0
#while acc < 101:
#    soma = soma + acc
#    acc +=1
#print(soma)

#exercicio 3 ⭐
##calcular o quadrado do 1 ao 10 com for
#i = 1
#for i in range(0,11):
#    resultado = i ** 2
#    i+=1
#    print(resultado)

#exercicio 4 ⭐
##Escreva um programa de 100 a 1 em ordem decrescente utilizando um laço de repetição while
#n = 101
#while n > 1:
#    n -= 1
#    print(n)






#exercicio 5 💔 não consegui porem acho qe entendi!
#fatorial com for
#fatorial = 1
#numero = int(input("Digite qual numero você quer saber o fatorial: "))
#numero_original = numero

#for i in range(numero, 0, -1):
#    fatorial = fatorial * i

#print(f"O fatorial de {numero_original} é {fatorial}")


#exercicio 6 ⭐
#escreva um programa que imprima numero de 1 a 50 usando while pulando de 5 em 5
#n = 0
#while n < 50:
#    n+=5
#    print(n)

#Exercicio 7 ⭐ com algumas olhadas no exercicio do for porem deu certo
 #Escreva um programa que solicite ao usuario um numero e imprima a tabuada desse numero de 1 a 10, utilizando o while
#n = 1
#numero = int(input("Escolha um número para ver sua tabuada e resultados: "))
#numero_original = numero
#while n <= 10:
#    print(f"A Tabuada do {numero_original}: ")
#    resultados = numero * n
#    print(f"{numero_original} x {n} = {resultados}")
#    n+=1

#EXERCICIO 8 ⭐💔 dei olhadas no exercicio ao contrario
#Escreva um programa que calcule a media de 5 numeros inseridos pelo usuario, usando um laço de repetição FOR
#soma = 0
#i = 0
#quantidade = 5
#for i in range (i, quantidade, 1):
#    numero = float(input(f"Indique o Numero {i + 1}: "))
#    soma += numero
#    i += 1
#    media = soma / quantidade
#print(f"A média dos {quantidade} numeros é de: {media}")
    
# EXERCICIO 9 -
#Escreva um programa que imprima os numeros primos de 1 a 100 utilizando a laço for
#print("Números primos de 1 a 100: ")  
#for n in range(1, 101):
#    eh_primo = True
#    for i in range(2, n):
#        if n % i == 0:
#            eh_primo = False
#            break
#    if eh_primo:
#        print(n)

# EXERCICIO 10 -
# escreva um programa que solicite ao usuário um número e imprima se ele é par ou ímpar, utilizando um laço de repetição while

#numero = (int(input("Digite um número para verificar se ele é impar ou par: ")))

#while numero >= 0:
#    if numero % 2 == 0:
#        print("É um numero par")
#    else:
#        print("É um numero impar")
#    numero = (int(input("Digite um número para verificar se ele é impar ou par: ")))

## Exercicio 11
#Soma dos numeros pares até um limite
#peça para o usuario para inserir um numero positivo inteiro. Em seguida, some todo os numeros pares ate esse limite usando while
#i = 0
#soma = 0
#n = int(input("Digite o número limite para a operação: "))
#while i <= n:
#    if i % 2 == 0:
#        soma += i
#    i += 1
#print(soma)
        
# EXERCICIO 12
# tabuada de um numero especifico usando for.
#Solicite ao usuario um numero inteiro. de 1 a 10 faça sua tabuada
#n = int(input("Digite um numero: "))  
#print(f"A tabuada do numero {n} é: ")

#for i in range(1, 11):
#    resultado = n * i
#    print(resultado)

#exercicio 13

    
    

