"""Peça uma lista de números e um número específico. Remova esse número da lista (se existir)."""
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
n = int(input("Informe o número que você deseja remover: "))

if n in numeros:
    numeros.remove(n)
    print(numeros)
else:
    print("Esse número não está na lista")
    
  