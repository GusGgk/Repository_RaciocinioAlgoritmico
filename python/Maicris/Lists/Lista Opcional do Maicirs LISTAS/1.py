"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
nums = []

for i in range(5):
    pergunta = int(input(f'Digite o {i+1} Número: '))
    nums.append(pergunta)
print(nums)

#help("__main__")