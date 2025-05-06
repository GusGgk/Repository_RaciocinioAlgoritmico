#Criar um programa que lê as temperaturas médias de cada mês do ano e as armazena em uma lista.
#Usar um outro vetor para guardar e exibir, quando necessário, os nomes dos meses do ano.
#Calcular a média anual de temperatura, e informar quais meses ficaram acima desta média anual
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
temp = []

for mes in meses:
    temperatura = int(input(f"Informe a Temperatura Média do Mês de {mes}: "))
    temp.append(temperatura) 
    
media = sum(temp)/len(temp)
print(f"\nA Média Anual de Temperatura é: {media}")

print("\n Meses Com temperatura Média Anual")

for i in range(len(temp)):
    if temp[i] > media:
        print(f"{meses[i]}: {temp[i]:.2f}*C")


    