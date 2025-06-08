"""Criar um programa que, fazendo uso de funções, cadastra
contatos em uma agenda telefônica, podendo excluir estes
contatos. Deve ser exibido um menu com as opções: inserir,
remover e sair.
"""

lista_contatos = []


def inserir():
    nome = input("Digite o nome que você deseja cadastrar: ")
    telefone = input("Digite o número de telefone dessa pessoa: ")
    contato = {"nome": nome, "telefone": telefone}
    lista_contatos.append(contato)
    
def remover():
    excluir = input("informe o número da pessoa que deseja excluir: ")
    for contato in lista_contatos:
        if contato ["telefone"] == excluir:
            lista_contatos.remove(contato)
            break
    

while True:
    print("\nMenu:")
    print("1 - Inserir contato")
    print("2 - Remover contato")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        inserir()
    elif opcao == "2":
        remover()
    elif opcao == "3":
        print("Saindo da agenda...")
        break
    else:
        print("Opção inválida. Tente novamente.")

    print(f"\nContatos atuais: {lista_contatos}")


