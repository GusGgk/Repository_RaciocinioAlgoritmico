"""Sintexe de uma função
def somar():
    pass"""
    
def get_fullname(name, *surnames):
    fullname = name
    for surname in surnames:
        fullname += " " + surname
    return fullname
    
name = get_fullname("Gustavo", "Giacoia", "Kumagai")
print(name)
#poderia guardar no banco de dados o nome completo