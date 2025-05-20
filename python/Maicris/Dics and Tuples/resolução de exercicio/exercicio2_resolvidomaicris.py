"""EXERCIXCIO 2
2. Criar um programa que cadastre funcionário de uma empresa e
seus dependentes. O funcionário deve ser cadastrado com
matrícula, nome e dependentes. Os dependentes devem ser
inseridos dinamicamente em uma tupla. Dica: usar o operador
+=."""

cadastros = []

while True:
    matricula = int(input("Digite a Matricula: "))
    nome = input("Digite o nome: ")
    dependentes = tuple()
    while True:
        dependente = input(f"Digite o nome do dependente\n(<enter>) para sair: ")
        if dependente == "":
            break
        dependentes += (dependente,)
    cadastro = {
        "matricula": matricula,
        "nome": nome,
        "dependentes": dependentes
    } 
    cadastros.append(cadastro)
    if input("Deseja continuar (s/n): ") == "n":
        break
print(cadastros)
            