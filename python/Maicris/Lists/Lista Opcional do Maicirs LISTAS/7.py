"""ENUNCIADO
7.Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
nums = []
for i in range(5):
    num = int(input(f"Digite o {i+1} Número: "))
    nums.append(num)
print(nums)

#soma
soma = sum(nums)
print(soma)

#mult
mult = 1
for n in nums:
    mult *= n
print(mult)

#help("__main__") 