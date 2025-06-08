"""Faça um programa que tenha uma função chamada escreva()
que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel
EX: escreva(Olá Mundo)
"""

def escreva(n):
    tamanho = len(n)
    print("-" * tamanho)
    print(n)
    print("-" * tamanho)
    

escreva("Olá Mundo")
escreva("AAAAAAAAAAAAAAAAAAAAAA")
