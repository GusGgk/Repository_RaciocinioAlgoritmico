l1 = float(input("Digite o primeiro lado do triângulo: "))
l2 = float(input("Digite o segundo lado do triângulo: "))
l3 = float(input("Digite o terceiro lado do triângulo: "))

if l1 == l2 == l3:
    print("equilatero")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("isoceles")
elif l1!= l2!= l3:
    print("escaleno")
else:
    print("vaitomanocu")