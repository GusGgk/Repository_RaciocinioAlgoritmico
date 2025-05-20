"""ENUNCIADO
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados,
faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;
"""
notas = []
while True:
    nota = float(input(f"Digite um numero(para parar digite -1): "))
    if nota != -1:
        notas.append(nota)
    else:
        break
#a
print(f"\n Questão A- Informe quantos números foram digitados: {len(notas)} ")

#b
print(f"\nQuestão B- Mostre a lista dos números informados: {notas}")

#c
print(f"\nQuestão C - Mostre a lista invertida uma abaixo da outra: ")
for i in range(len(notas) -1,-1,-1):  
    print(notas[i])

#d
print(f"\nQuestão D - A soma de todos os itens informados é: {sum(notas)}")

#e
media = sum(notas)/len(notas)
print(f"\n Questão E - Calcular as médias dos números informados, e a média é: {media:.2f}")

#f
print(f"\nQuestão F - Calcular o número de valores acima da media")
contador_cima = 0
for nota in notas:
    if nota > media:
        contador_cima += 1
print(f"Quantidade de valores acima da média: {contador_cima} números")
      
#g
print(f"\nQuestão G - Calcular o número de valores abaixo de 7")
contador_baixo_de_sete = 0
for nota in notas:
    if nota < 7:
        contador_baixo_de_sete +=1
print(f"A quantidade de números abaixo de 7 é: {contador_baixo_de_sete} números ")

#h
print("--- ENCERRANDO O PROGRAMA ---")



#help("__main__")