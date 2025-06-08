"""ENUNCIADO
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
notes =[]
for i in range(4):
    note = float(input(f"Digite a {i+1}° nota: "))
    notes.append(note)
print(f"A lista de notas é: {notes}")

print(f"MÉDIA DAS 4 NOTAS")
media = sum(notes)/len(notes)
print(media)

#help("__main__")