"""Cadastro De usuário
"""
users = []
while True:
    cpf = input("Digite o CPF do usuário: ")
    name = input("Digite o nome do usuário: ")
    age = input("Digite a idade do usuário: ")
    user = {"cpf": cpf,"nome": name, "idade": age}
    users.append(user)
    if input("Deseja continuar?(s/n): ") == "n":
        break
print(users) #[{'cpf': '1234', 'nome': 'gk', 'idade': '14'}, {'cpf': '123456', 'nome': 'gkk', 'idade': '12'}]
print("*** Lista de Usuários ***")
for user in users:
    #print(user) #*** Lista de Usuários ***
                #{'cpf': '14976568938', 'nome': 'Gustavo', 'idade': '18'}
                #{'cpf': '123456789', 'nome': 'Malu', 'idade': '18'}
    for key, value in user.items():
        print(f"{key}: {value}")
    print("----------------")
#*** Lista de Usuários ***
#cpf: 1234
#nome: gk
#idade: 14
#----------------
#cpf: 123456
#nome: gkk
#idade: 12
#----------------