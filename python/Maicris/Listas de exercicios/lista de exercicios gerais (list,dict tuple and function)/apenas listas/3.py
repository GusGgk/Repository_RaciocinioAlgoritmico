"""Crie uma lista com 5 nomes e ordene em ordem alfabética."""

nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}°Nome:  ")
    nomes.append(nome)
    
print(nomes)

nomes.sort()

print(nomes)
