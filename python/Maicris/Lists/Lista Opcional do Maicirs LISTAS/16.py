"""ENUNCIADO
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um
vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um
total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores
receberam salários nos seguintes intervalos de valores:
a. $200 - $299
b. $300 - $399
c. $400 - $499
d. $500 - $599
e. $600 - $699
f. $700 - $799
g. $800 - $899
h. $900 - $999
i. $1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados."""



contadores = [0] * 9

while True:
    vendas = float(input("Digite o valor das vendas brutas do vendedor ( ou aperte -1 para sair): "))
    if vendas == -1:
        break
    
    salario = 200 + 0.09 * vendas
    
    indice = int(salario//100) - 2
    if indice >= 8:
        indice = 8
    elif indice < 0:
        indice = 0
    
    contadores[indice] += 1

print("\nDistribuição de salários:")
for i in range(8):
    print(f"${200 + i*100} - ${299 + i*100}: {contadores[i]} vendedor(es)")
print(f"$1000 ou mais: {contadores[8]} vendedor(es)")
