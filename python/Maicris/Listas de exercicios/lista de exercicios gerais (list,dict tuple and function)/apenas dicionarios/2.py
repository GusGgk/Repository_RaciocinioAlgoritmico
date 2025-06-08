""" Peça ao usuário um nome e mostre a nota correspondente no dicionário"""

alunos = {
    "Gustavo":9.0,
    "Dosan":8.5,
    "André":9.4,  
}



nome = input("Digite um nome de algum aluno: ")


if nome in alunos:
    print(f"A nota do aluno {nome} é {alunos[nome]}")
else:
    print("Aluno não encontrado.")