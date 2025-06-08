"""Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de
uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar
estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa
que a chamou.
O programa deverá então exibir o valor a ser pago na tela.
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a
prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade
e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma.
Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso."""


def valorPagamento(prestacao, dias_atrasados):

    if dias_atrasados == 0:
        return prestacao
    else:
        multa = 0.03 * prestacao 
        juros = (0.001 * prestacao) * dias_atrasados
        valor_final = multa + prestacao + juros
        return valor_final
       

contador = 0
total_pago = 0
 
while True:
        prestacao = float(input("Qual o valor que deve ser pago na  sua prestação (digite 0 para sair)? "))
        if prestacao == 0:
            break
        else:
            dias_atrasados = int(input("Quantos dias em atraso está a prestação? "))
            valor_a_pagar = valorPagamento(prestacao, dias_atrasados)
            print(f" Você deverá pagar: R$ {valor_a_pagar:.2f}")
            total_pago += valor_a_pagar
            contador += 1

#relatorio
print(f"Quantidade de prestações pagas: {contador}")
print(f"Valor total pago: {total_pago}")