"""Crie um dicionário onde as chaves são os nomes dos alunos e os valores são as notas. Depois,
mostre todos os alunos com suas notas.
"""

alunos = {}

for _ in range(3):  
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    alunos[nome] = nota

for nome in alunos:
    print(nome, ":", alunos[nome])
