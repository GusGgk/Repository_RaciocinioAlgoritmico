nums = []
while True:
    num = int(input("Digite um número (0 Sair): "))
    if num == 0:
        break
    nums.append(num)
    
for num in nums: # print da lista
    print(num)

for i in range(len(nums)): # repete a lista
    print(nums[i])
    
print(nums) #lista empacotada
print(*nums) # desempacotar lista


