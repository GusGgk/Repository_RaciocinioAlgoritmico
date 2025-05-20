"""ENUNCIADO
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto"," Setembro", "Outubro", "Novembro", "Dezembro"]
temperatura_media_meses = []

for i in range(12):
    temperatura = float(input(f"Digite a temperatura média do mês de {meses[i]}: "))
    temperatura_media_meses.append(temperatura)
    
media_anual = sum(temperatura_media_meses) / len(temperatura_media_meses)
print(f"A media anual é: {media_anual:.2f}")

print(f"Os meses que ficaram acima da média atual são: ")
for i in range(len(meses)):
    if temperatura_media_meses[i] > media_anual:
        print(f"{meses[i]}")   

#help("__main__")

