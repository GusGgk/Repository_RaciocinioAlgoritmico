def menu(cardapio):
    print("Bem-Vindo ao Restaurante Boca Feliz!!!")
    print("*** CARDÁPIO ***")
    for produto in cardapio:
        print(produto)

def verificar_estoque(ingredientes,estoque):
   print() 

def executar_pedido(pedido, cardapio,estoque):
    ingredientes = cardapio[pedido]
    vender = verificar_estoque(ingredientes,estoque)
    msg = ""
    for ingrediente in ingredientes:
        if estoque[ingrediente] <= 0:
            msg += "Infelizmente acabou o {ingrediente}\n"
            vender = False
            
        if vender:
            msg = f"Um {pedido} saindo no capricho!!!"
            for ingrediente in ingredientes:
                estoque[ingrediente] -= 1
        else:
            return msg


def pedido(cardapio, estoque):
        pedido = input("O que deseja pedir(0 para sair)? ")
        if pedido == "0":
            
            return True, "Obrigado e volte sempre!"
        elif pedido not in cardapio:
            return False, "Item não localizado no cardápio"
        else:
            return False, executar_pedido(pedido, cardapio, estoque)
            

def sistema(cardapio, estoque):
    while True:
        menu(cardapio)
        sair, msg = pedido(cardapio, estoque)
        print(msg)
        if sair:
            break    



c = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}
e = {'pao': 10, 'hamburguer': 13, 'tomate': 5, 'bacon': 5, 'ovo': 5}
sistema(c, e)