"""ENUNCIADO
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0"""

mediaDosAlunos = []
nomeDosAlunos = []
matrizNotas = []

#nome dos alunos
for i in range(10):
    nome = input(f"Digite o nome do {i+1} Aluno: ")
    nomeDosAlunos.append(nome)
    matrizNotas.append([])
print("--- NOME DOS ALUNOS ---")
print(f"\n",nomeDosAlunos)

#guardar as 4 notas de cada aluno em matriz de nota
for i in range(10):
    for j in range(4):
        nota = float(input(f"Digite a {j+1}ª nota de {nomeDosAlunos[i]}: "))
        matrizNotas[i].append(nota)
print(f"\n--- AS 4 NOTAS DE CADA ALUNO ---")
print(matrizNotas)

#media de cada aluno
for notas in matrizNotas:
    media = sum(notas)/len(notas)
    mediaDosAlunos.append(media)
print(f"\n--- MÉDIA DE CADA ALUNO ---")
for i in range(10): 
    print(f"\nMédia do aluno {nomeDosAlunos[i]} é: {mediaDosAlunos[i]:.2f} ")

#aprovados
alunos_aprovados = sum(1 for media in mediaDosAlunos if media >= 7)
print(f"\nO número de alunos aprovados é: {alunos_aprovados}")

#help("__main__") 