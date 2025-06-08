"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um
item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas."""

def somaImposto(taxaImposto, custo):
    custo_com_imposto = custo + (custo * taxaImposto / 100)
    return custo_com_imposto

custo = float(input("Digite o custo do item: "))
taxa = float(input("Digite a taxa de imposto (%): "))

novo_custo = somaImposto(taxa, custo)


print(f"O custo com imposto é: R${novo_custo:.2f}")
