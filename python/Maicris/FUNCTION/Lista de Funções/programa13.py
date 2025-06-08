"""Desenha moldura. 
Construa uma função que desenhe um retângulo usando os caracteres + , - e | . Esta
função deve receber dois parâmetros, linhas e colunas,
sendo que o valor por omissão é o valor mínimo igual a 1
e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores
dentro da faixa de forma elegante."""

def retangulo(linhas,colunas):
    linhas = max(1,min(linhas,20))
    colunas= max(1, min(colunas,20))
    
    print(f"+" + "-" * (colunas - 2) + "+" if colunas > 1 else "+")
    
    for _ in range(linhas - 2):
        print("|" + " " * (colunas-2) + "|" if colunas > 1 else "|")
    
    if linhas > 1:
        print(f"+" + "-" * (colunas - 2) + "+" if colunas > 1 else "+")
    
    
    
retangulo(5,10)
retangulo(10,10)
retangulo(20,20)