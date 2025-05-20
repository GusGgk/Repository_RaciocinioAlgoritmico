nums = []

maior = []
menor = []

for i in range(6):
    num = int(input(f"Informe o {i+1} Número: "))
    nums.append(num)

media = sum(nums)/len(nums)
print(f"A média dos 6 números é: {media} ")

for num in range(len(nums)):
    if nums[num] > media:
        maior.append(nums[num])
    else:
        menor.append(nums[num])

print(f"Números maiores que a Média: {maior} ")
print(f"Números menores que a média: {menor}")
