"""ENUNCIADO
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200
mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode
aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá
receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse
o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação
igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100
Situação Quantidade Percentual
1- necessita da esfera 40 40%
2- necessita de limpeza 30 30%
3- necessita troca do cabo ou conector 15 15%
4- quebrado ou inutilizado 15 15%"""

lista_defeitos = ["1 - Necessita da esfera",
                  "2 - Necessita de limpeza",
                  "3 - Necessita troca do cabo ou conector",
                  "4 - Quebrado ou inutilizado"
]

contagem_defeitos = [0,0,0,0]
ids = []

while True:
    mouse = int(input("Informe o id do mouse(para sair pressione 0): "))
    if mouse == 0:
        break
    else:
        ids.append(mouse)
    print(f"\n {lista_defeitos}" )
    defeito = int(input(f"\nInforme o defeito do seu mouse de acordo com a lista acima: "))
    if 1 <= defeito <= 4:
        contagem_defeitos[defeito - 1] += 1
    else:
        print("Informe um número válido entre 1 e 4.")

        

#quantidade de mouses
total_mouses = len(ids)
print(f"Quantidade de mouses: {total_mouses}")  
 
print(f"( {"Situação":<30} {"Quantidade":<15} {"Percentual"}%)")
for i in range(len(lista_defeitos)):
    nome_defeito = lista_defeitos[i][4:]  # remove o "1 - ", "2 - ", etc.
    quantidade = contagem_defeitos[i]
    percentual = (quantidade / total_mouses) * 100
    print(f"{i+1}- {nome_defeito:<30} {quantidade:<20} {percentual:.0f}%")      
    