"""
Tupla
"""
users = [
    {"cpf": "14976568938", "nome": "Gustavo"},
    {"cpf": "12345789098","nome": "Malu"},
    
]
info = input("Qual usuario deseja localizar? (cpf): ")
found = False

for user in users:
    if info == user["cpf"]:
        user = (user["cpf"], user["nome"])
        print(user)
        found = True
        #Qual usuario deseja localizar? (cpf): 14976568938
        #{'cpf': '14976568938', 'nome': 'Gustavo'}
        # ('14976568938', 'Gustavo') com esse novo codigo
if not found:
    print("Usuario não encontrado!")
#Qual usuario deseja localizar? (cpf): 14
#Usuario não encontrado!