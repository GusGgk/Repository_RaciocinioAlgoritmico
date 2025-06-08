"""Leia uma lista de notas e calcule a média"""

notas = []

while True:
    nota = float(input("Informe uma nota(101 para sair): "))
    if nota == 101:
        break
    notas.append(nota)
    
media = sum(notas) / len(notas)

print(notas)
print(media)
