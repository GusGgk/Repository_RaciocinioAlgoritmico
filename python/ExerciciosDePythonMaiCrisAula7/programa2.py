l1 = []
l2 = []
l3 = []

for i in range(5):
    op1 = int(input(f"Lista 1 -Digite o {i+1} numero: "))
    l1.append(op1)
print(l1)

for i in range(5):
    op2 = int(input(f"Lista 2 - Digite o {i+1} numero: "))
    l2.append(op2)
print(l2)

for i in range(len(l1)):
    l3.append(l1[i])
    l3.append(l2[i])
print(l3)