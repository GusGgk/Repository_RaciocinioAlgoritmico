"""
Correndo um dicionario
"""
gustavo = {
    "nome": "Gustavo",
    "idade": 18,
    "Cidade": "Praia Grande",
    "Fumante": False
}

for info in gustavo:
    print(info) #nome
                #idade
                #Cidade
                #Fumante
                
for info in gustavo.values():
    print(info)
#Gustavo
#18
#Praia Grande
#False

for key, value in gustavo.items():
    print(f"Chave: {key} - Valor: {value} ")
#Chave: nome - Valor: Gustavo
#Chave: idade - Valor: 18
#Chave: Cidade - Valor: Praia Grande
#Chave: Fumante - Valor: False