"""ENUNCIADO
ma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de
arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos
usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele
conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre 456123789
anderson 1245698456
antonio 123456456
carlos 91257581
cesar 987458
rosemary 789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que
gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc. Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr. Usuário Espaço utilizado % do uso
1 alexandre 434,99 MB 16,85%
2 anderson 1187,99 MB 46,02%
3 antonio 117,73 MB 4,56%
4 carlos 87,03 MB 3,37%
5 cesar 0,94 MB 0,04%
6 rosemary 752,88 MB 29,16%
Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes
deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do
percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal."""


dados = [
    "alexandre 456123789",
    "anderson 1245698456",
    "antonio 123456456",
    "carlos 91257581",
    "cesar 987458",
    "rosemary 789456125"
]

nomes = []
espacos_mb = []


for linha in dados:
    partes = linha.split()
    nome = partes[0]
    espaco_bytes = int(partes[1])
    espaco_mb = espaco_bytes / (1024 * 1024)  # conversão direta
    nomes.append(nome)
    espacos_mb.append(espaco_mb)


total_uso = sum(espacos_mb)
media_uso = total_uso / len(espacos_mb)


print("ACME Inc. Uso do espaço em disco pelos usuários")
print("------------------------------------------------------------")
print("Nr.  Usuário        Espaço utilizado     % do uso")
print()


for i in range(len(nomes)):
    percentual = (espacos_mb[i] / total_uso) * 100
    print(f"{i+1:<4} {nomes[i]:<15} {espacos_mb[i]:>10.2f} MB {percentual:>10.2f}%")


print(f"\nEspaço total ocupado: {total_uso:.2f} MB")
print(f"Espaço médio ocupado: {media_uso:.2f} MB")
