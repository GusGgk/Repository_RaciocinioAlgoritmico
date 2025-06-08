"""Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."""

def quantidade_numero():
    n = input("Digite algum número: ")
    n= n.replace("-","")
    n= n.replace(".","")
    quantidade=  len(n)
    return quantidade


print(f"A quantidade de números digitados é: {quantidade_numero()}")

    