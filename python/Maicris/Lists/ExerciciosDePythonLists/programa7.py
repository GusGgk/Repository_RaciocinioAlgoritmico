"""
Dado o vetor nums = [3, 11, 6, 32, 15, 22, 4, 10, 5], criar uma
matriz 3x3 com os 3 maiores elementos na primeira linha, os 3
elementos intermediários na segunda linha, e os elementos
menores na terceira linha.

"""
nums = [3, 11, 6, 32, 15, 22, 4, 10, 5]
print(nums)
nums.sort(reverse=True)
print(nums)


matriz = []
linha = []

for i in nums:
    linha.append(i)
    if len(linha) == 3:
        matriz.append(linha)
        linha = []
        
for linha in matriz:
    print(linha)
        
            


