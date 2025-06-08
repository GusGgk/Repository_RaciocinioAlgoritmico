"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa
deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma
para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor 'A’ para A.M. e 'P’ para
P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua
um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar."""

def conversao(hora, minuto):
    if hora == 0:
        hora_convertida = 12
        periodo = "A"
    elif 1<= hora <= 11:
         hora_convertida = hora
         periodo = "A"
    elif hora == 12:
        hora_convertida = 12
        periodo = "P"
    else:
        hora_convertida = hora - 12
        periodo = "P"
    
    return hora_convertida, minuto, periodo
        
    

def exibir_horario(hora_convertida, minuto, periodo):
    if periodo == 'A':
        sufixo = 'A.M.'
    else:
        sufixo = 'P.M.'
    
    print(f"{hora_convertida}:{minuto:02d} {sufixo}")


while True:
    hora = int(input("Digite a hora (0-23): "))
    minuto = int(input("Digite o minuto (0-59): "))
    
    hora_convertida, minuto, periodo = conversao(hora, minuto)
    
    exibir_horario(hora_convertida, minuto, periodo)
    
    repetir = input("Deseja converter outro horário? (s/n): ")
    if repetir.lower() != 's':
        break
