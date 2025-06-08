l1 = float(input("Digite o primeiro lado do triângulo: "))
l2 = float(input("Digite o segundo lado do triângulo: "))
l3 = float(input("Digite o terceiro lado do triângulo: "))

if l1 == l2 and l2 == l3 and l3 == l1:
    print("Equilátero")
elif l1 == l2 or l1 == l3 or l3 == l2:
    print("Isoceles")
else:
    print("escaleno")
    
