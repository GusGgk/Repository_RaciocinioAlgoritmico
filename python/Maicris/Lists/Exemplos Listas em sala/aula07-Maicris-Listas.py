"""
Criando Listas
"""

nums = []
for i in range(5):
    num = int(input(f"Digite o {i+1} numero: "))
    nums.append(num)
print(nums)
for num in nums:
    print(num)   
soma = sum(nums) 
print(soma)
media = sum(nums)/len(nums)
print(media)