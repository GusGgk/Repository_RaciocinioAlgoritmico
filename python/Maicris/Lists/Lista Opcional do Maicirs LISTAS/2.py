"""ENUNCIADO
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

nums = []
for i in range(10):
    n = int(input(f"Informe o {i+1}° Numero: "))
    nums.append(n)
 
print("A ordem normal da lista:")   
print(nums)

nums.reverse()
print("A lista inversa:")
print(nums)
#help("__main__")