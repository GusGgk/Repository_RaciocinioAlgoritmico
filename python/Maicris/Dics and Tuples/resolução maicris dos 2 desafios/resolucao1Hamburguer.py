estoque = {'pao': 10, 'hamburguer': 13, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

while True:
    print("Bem-Vindo ao Restaurante Boca Feliz!!!")
    print("*** CARDÁPIO ***")
    for produto in cardapio:
        print(produto)
    pedido = input("O que deseja pedir(0 para sair)? ")
    if pedido == "0":
        print("Obrigado e volte sempre!")
        break
    elif pedido not in cardapio:
        print("Item não localizado no cardápio")
    else:
        ingredientes = cardapio[pedido]
        vender = True
        for ingrediente in ingredientes:
            if estoque[ingrediente] <= 0:
                print(f"Infelizmente acabou o {ingrediente}.")
                vender = False
            
            if vender:
                print(f"Um {pedido} saindo no capricho!!!")
                for ingrediente in ingredientes:
                    estoque[ingrediente] -= 1