"""ENUNCIADO
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idades =[]
alturas = []
pessoas = []
guardarTudo = []

for i in range(5):
    pessoa = input(f"Informe o nome da {i+1} pessoa: ")
    pessoas.append(pessoa)
print(pessoas)

for i in range(5):
    idade = int(input(f"Qual a idade de {pessoas[i]}? "))
    idades.append(idade)

print(idades)
print(f"As idades invertidas são:")
idades.reverse()
print(idades)

for i in range(5):
    altura = float(input(f"Em cm qual é a altura de {pessoas[i]}? "))
    alturas.append(altura)
print(alturas)

print(f"As alturas invertidas são:")
alturas.reverse()
print(alturas)

for i in range(5):
    guardarTudo.append([pessoas[i], idades[i], alturas[i]])
print(guardarTudo)


#help("__main__")