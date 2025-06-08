"""
Calcular as raízes de um polinomio do segundo grau a partir da formula de baskara
y = f(x) = ax^2 + bx + c
delta = b^2 - 4ac
x'= (-b + raiz(delta)) / 2a
x''= (-b - raiz(delta)) / 2a
"""
import math

def calc_delta(a,b,c):
    return b**2 - 4*a*c

def calc_root(a, b , delta, signal = 1):
    return (-b + signal * math.sqrt(delta)) / (2*a)


def baskara(a, b, c):
    delta = calc_delta(a,b,c)
    if delta < 0:
        return None, None
    elif delta == 0:
        return calc_root(a,b,delta)
    else:
        x1 = calc_root (a,b,delta)
        x2 = calc_root(a,b,delta, -1)
        return x1, x2
    


x1, x2 = baskara(1,1,1)
print(f"Valor das raízes: {x1} e {x2}")