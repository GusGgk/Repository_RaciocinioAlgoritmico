"""Data com mês por extenso.
Construa uma função que receba uma data no formato DD/MM/AAAA
e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida"""
meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro")



def data():
    while True:
        dia = int(input("Informe algum dia do ano (1-31): "))
        if dia < 1 or dia > 31:
            print("dia invalido, tente novamente")
            continue
        
        mes = int(input("Informe um mês(1-12): "))
        if mes < 1 or mes > 12:
            print("mês inválido, tente novamente")
            continue
        
        ano = int(input("Informe o ano (AAAA): "))
        if ano > 9999:
            print("Ano muito longo me desculpe!")
            continue
        
        
        return dia,mes,ano

dia, mes, ano = data()
mes_extenso = meses[mes-1]

print("DIFERENTES JEITOS PARA A DATA")
print(f"{dia:02d}/{mes:02d}/{ano}")
print(f"{dia} de {mes_extenso} de {ano}")


