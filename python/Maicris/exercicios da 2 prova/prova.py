"""Calcular a area do cilindro, 3 funções e chamar 2 dentro de outra"""

r = float(input("Digite o raio do cilindro: "))
h = float(input("Digite a altura do cilindro: "))
pi = 3.14

def area_lateral():
    return (2*pi)*r*h

def area_das_bases():
    base = (2*pi)*(r**2) 
    return base

def area_total():
    total = area_lateral() + area_das_bases()
    return total

print(f"De acordo com o raio {r} e a altura {h}, as areas do cilindro são: ")

print(f"A area lateral: {area_lateral()} e a area da base: {area_das_bases()}")

print(f" E por ultimo a area total do cilindro é {area_total()}")
