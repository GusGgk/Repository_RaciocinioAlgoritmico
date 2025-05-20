"""ENUNCIADO
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
nums = [i for i in range(1, 21)]
print(nums)

impares = []
pares = []

for i in nums:
    if i % 2 == 0:
        pares.append(i)
    
    else:
        impares.append(i)
    
    
print(f"Os números pares são: {pares}")
print(f"Os números impares são: {impares}")

#help("__main__") 