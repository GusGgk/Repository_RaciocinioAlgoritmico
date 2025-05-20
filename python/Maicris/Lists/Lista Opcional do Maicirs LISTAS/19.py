"""ENUNCIADO
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não
deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das
opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa
deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída
foi dado pela empresa, e é o seguinte:

Sistema Operacional Votos %
------------------- ----- ---
Windows Server 1500 17%
Unix 3500 40%
Linux 3000 34%
Netware 500 5%
Mac OS 150 2%
Outro 150 2%
------------------- -----
Total 8800
O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40%
dos votos."""

sistemas_operacionais = ["1 - Windows Server","2 - Unix","3 - Linux","4 - Netware","5 - Mac OS","6 - Outros"]
sistemas_votados = []

while True:
    print("\nEscolha o melhor Sistema Operacional para uso em servidores:")
    
    for sistema in sistemas_operacionais:
        print(sistema)
    print("0 - Encerrar votação")
    voto = int(input("Digite sua opção: "))
    if voto == 0:
        break
    elif 1 <= voto <= 6:
        sistemas_votados.append(voto)
    else:
        print("Opção Inválida. Tente novamente de 1 a 6.")
print(sistemas_votados)

total_votos = len(sistemas_votados)


def calcular_percentual(votos, total):
    return(votos/total) * 100
votos_por_sistema = [0,0,0,0,0,0]

for voto in sistemas_votados:
    votos_por_sistema[voto - 1] += 1
print(f"\n Sistema Operacional    Votos    %")
print(f"----------------------    -----   ---")
mais_votos = 0
indice_mais_votado = 0

for i in range(6):
    nome = sistemas_operacionais[i][4:]
    votos = votos_por_sistema[i]
    percentual = calcular_percentual(votos, total_votos)
    
    print(f"{nome:<22} {votos:<8} {percentual:.1f}%")
    
    if votos > mais_votos:
        mais_votos = votos
        indice_mais_votado = i


nome_mais_votado = sistemas_operacionais[indice_mais_votado][4:]  
percentual_mais_votado = calcular_percentual(mais_votos, total_votos)

print(f"\nO Sistema Operacional mais votado foi o {nome_mais_votado}, com {mais_votos} votos, correspondendo a {percentual_mais_votado:.1f}% dos votos.")
    