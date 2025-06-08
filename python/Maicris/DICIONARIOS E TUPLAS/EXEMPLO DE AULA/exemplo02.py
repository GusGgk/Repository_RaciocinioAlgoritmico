"""USANDO DICIONARIO COMO REGISTRO"""

gustavo = {
    "nome": "Gustavo",
    "idade": 18,
    "Cidade": "Praia Grande",
    "Fumante": False
}
print(gustavo) # {'nome': 'Gustavo', 'idade': 18, 'Cidade': 'Praia Grande'}

print(gustavo.keys()) #dict_keys(['nome', 'idade', 'Cidade'])
print(gustavo.values()) # dict_values(['Gustavo', 18, 'Praia Grande'])
print(gustavo.items()) # dict_items([('nome', 'Gustavo'), ('idade', 18), ('Cidade', 'Praia Grande'), ('Fumante', False)]) ele entrega tuplas

