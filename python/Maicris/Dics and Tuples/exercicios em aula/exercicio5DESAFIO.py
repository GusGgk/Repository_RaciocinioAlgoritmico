"""ENUNCIADO DO DESAFIO
Criar um programa que solicita valor de vendas e o mês onde
cada venda ocorreu. Independente de repetição de meses, o
aplicativo deve totalizar por mês todas as vendas cadastradas.
Ao final deve informar o valor de vendas de todos os meses do
ano. Obs.: se for digitado errado o nome do mês, informar que o
mês é inválido. FEITO EM AULA COM MAICRIS"""

sales = {"jan": 0,"fev": 0,"mar": 0,"abr": 0,
          "maio": 0,"jun": 0,"jul": 0,"ago": 0,
          "set": 0,"out": 0,"nov": 0,"dez": 0,
}

while True:
    value = float(input("Qual o valor da venda: (se for = 0 sai) "))
    if value == 0:
        break
    month = input("Qual o mês da venda? ")
    if month not in sales:
        print("Mês digitado inválido\n Use o nome do mês abreviado.")
    else:
        sales[month] += value
        
        
for month, total in sales.items():
    print(f"{month}: R$ {total:.2f}")


