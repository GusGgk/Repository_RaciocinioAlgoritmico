"""Enunciado
Criar um programa que efetua cadastro de produtos e preços. Caso o
produto já existe, pergunta se o usuário pretende atualizar o valor.
Imprimir o dicionário ao final do programa em formato de lista. """

"""menu = {
    "Arroz": 10,
    "Feijão": 8.90,
    "Farofa": 4.60,
}"""

menu = {
    
}
while True:
    produto = input("Digite o nome do produto(0 = sair): ")
    if produto == "0":
        break
    else:
        if produto not in menu:
            preco = float(input("Digite o preço: "))
            menu[produto] = preco
        else:
            print("Esse produto já está cadastrado!")
            print(f"Seu preço atual é de: R$ {menu[produto]:.2f}")
        
            atualizar = input("Deseja atualizar o preço?(s/n): ").lower()
            if atualizar == "s":
                novo_preco = float(input("Digite o novo preço: "))
                menu[produto] = novo_preco

    print('\n --- Lista de produtos Cadastrados ---')
    for produto, preco in menu.items():
        print(f"Produto: { produto} |  Preço: R$ {preco:.2f}")
                
    

