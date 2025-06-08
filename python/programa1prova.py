"""Criar um dicionario e pedir nome e quantidade, ai tinha que ir atualizando a quantidade do item no dicionario"""

estoque = {}


while True:
    item = input("Digite o nome do produto(digite sair para fechar o programa): ")
    if item == "sair":
        break
    quantidade = int(input(f"Digite a quantidade do {item}: "))
    if item in estoque:
        estoque[item] += quantidade
    else:
        estoque[item] = quantidade
    print(estoque)
    entrada = input("Deseja Continuar?(s/n): ").lower()
    if entrada == "n":
        print(estoque)
        break
        
for key, value in estoque.items():
    print(f"{key} : {value}")
    

