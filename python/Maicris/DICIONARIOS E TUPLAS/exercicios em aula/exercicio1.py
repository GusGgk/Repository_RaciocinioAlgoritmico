"""ENUNCIADO
1. Criar um programa que efetua o cadastro de pessoas com nome,
rg e cpf por meio de tuplas, adicionando elas a uma lista.
Imprimir a lista ao final do programa."""

list_users = []

while True:
    
    name = input("Digite o nome do usuário: ")
    if name == "0":
        break
    rg = int(input("Digite os números do rg: "))
    
    cpf = int(input("Digite o cpf do usuário: "))
    
    user = (name,rg,cpf)
    list_users.append(user)
    
print(f"\n------------- Lista de Usuarios -----------")
print(list_users)

print(F"\n----------- LISTA COM DADOS SEPARADOS ----------")
for i in list_users:
    name, rg, cpf = i
    print(f"Nome: {name}  |  RG: {rg}  |  CPF: {cpf}")
