"""Sistema de Cadastro de usuarios"""

def show_menu(menu):
    print("*** MENU PARA CADASTRO DE SHOWS ***")
    for item in menu:
        print(item)
        

def user_cad(users: dict):
    cpf = input("Digite o CPF: ")
    if cpf in users:
        return False
    else:
        nome = input("Digite o  nome do Usuário: ")
        age = get_int_value("Digite a idade do usuário: ", 1, 130)
        city = input("Digite a cidade do usuário: ")
        user =  {
            "nome": nome,
            "idade": age,
            "cidade": city,
        }
        users[cpf] = user
        return True

def user_edit():
    pass

def user_remove():
    pass

def user_list(users: dict):
    print("\n*** Usuários Cadastrados ***")
    for cpf in users:
        print(f"CPF: {cpf}")
        user = users[cpf]
        print(f"Nome: {user['nome']}")
        print(f"Idade: {user['idade']}")
        print(f"Cidade: {user['cidade']}\n")
    print(" *** FIM DA LISTAGEM ***")


def sistema(menu, users):
    while True:
        show_menu(menu)
        op = get_int_value("Opção: ", 1, len(menu))
        if op == 1:
            if user_cad(users):
                print("Usuário cadastrado com sucesso!!!")
            else:
                print("Usuario ja cadastrado!!!")
        elif op == 2:
            user_edit()
        elif op == 3:
            user_remove()
        elif op == 4:
            user_list(users)
        elif op == 5:
            break
        else:
            print("Opção invalida!")
            
def get_int_value(msg, min, max):
    while True:
        try:
            op = int(input(msg))
            if op >= min and op <= max:
                return op
            else:
                print(f"Escolha uma opção entre {min} e {max}")
        except:
            print("Opção Invalida!!!")

    
menu_do_sistema = (
    "1. Cadastrar Usuário",
    "2. Editar Usuário",
    "3. Remover Usuário",
    "4. Listar Usuário",
    "5. Sair do Sistema",
)

users_dict ={
    
        "14976568938":{
        "nome": "Maicris",
        "idade": 39,
        "cidade": "Curitiba",
        },
        "123516171":{
        "nome": "Gustavo",
        "idade": 19,
        "cidade": "Curitiba",  
        }
    }
    

sistema(menu_do_sistema,users_dict)
