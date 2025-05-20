nome = "Gustavo"

for letra in nome:
    print(letra)
    if letra in "aeiou":
        print(f"Vogal Encontrada: {letra}")
        
print("-"*20)
print(nome[0])
# nome[0] = "R" iria dar erro pois não é mutavel


