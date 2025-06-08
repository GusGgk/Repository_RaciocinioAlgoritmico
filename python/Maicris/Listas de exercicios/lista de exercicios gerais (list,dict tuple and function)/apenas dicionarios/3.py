"""Peça para o usuário atualizar a nota de um aluno no dicionário"""
alunos = {
    "Gustavo":9.0,
    "Dosan":8.5,
    "André":9.4,  
}

print(alunos)
att = input("Digite o aluno da lista para alterar a nota: ")

if att in alunos:
    print(f"A nota atual do {att} é: {alunos[att]}")
    nova_nota = float(input("Digite a nova nota do aluno: "))
    alunos[att] = nova_nota
    print(f"A nova nota de {att} é {nova_nota}")
    
else:
    print("Aluno não encontrado")
 
print(alunos)   