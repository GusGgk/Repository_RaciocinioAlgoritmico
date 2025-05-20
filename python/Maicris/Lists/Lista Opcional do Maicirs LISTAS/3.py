"""ENUNCIADO
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
notes =[]
for i in range(4):
    note = float(input(f"Digite a {i+1} Nota: "))
    notes.append(note)
print(notes)

media = sum(notes)/len(notes) 
print(f"A média das 4 notas são: ")
print(media)

#help("__main__")