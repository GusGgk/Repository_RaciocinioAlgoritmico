"""
Criar um programa que solicite o nome de 4 times de futebol. O
programa deve simular partidas de forma que cada time jogue
uma vez com os outros 3 times. Na partida deve perguntar
quantos gols fez cada time, e somar as devidas pontuações. Ao
final deve dizer qual ou quais times foram campeões, uma vez
que pode haver empate em pontuação. Obs.: vitória vale 3
pontos para o vencedor, empate vale 1 ponto para cada time e
derrota não soma pontos.

"""
times = []

for i in range(4):
    nome_time = input(f"Digite o {i+1}º Time: ")
    times.append([nome_time, 0])
    
print("\n--- INCIANDO AS PARTIDAS ---")

for i in range(4):
    for j in range(i + 1, 4):
        time1_nome = times[i][0]
        time2_nome = times[j][0]
        print(f"\n Partida: {time1_nome} x {time2_nome}")
        
        
        gols_time1 = int(input(f"Digite quantos gols o {time1_nome} fez na partida? "))
        gols_time2 = int(input(f"Digite quantos gols o {time2_nome} fez na partida? "))
        
        if gols_time1 > gols_time2:
            print(f"{time1_nome} VENCEU!")
            times[i][1] += 3
        elif gols_time2 > gols_time1:
            print(f"{time2_nome} VENCEU!")
            times[j][1] += 3
        else:
            print("EMPATE!")
            times[i][1] += 1
            times[j][1] += 1
print(times)

# Organizando o ranking (ordena do maior para o menor em pontuação)
for i in range(len(times)):
    for j in range(i + 1, len(times)):
        if times[j][1] > times[i][1]:
            times[i], times[j] = times[j], times[i]

print("\n--- RANKING FINAL ---")
for i in range(4):
    print(f"{i+1}º lugar: {times[i][0]} - {times[i][1]} pontos")

# Descobrindo o(s) campeão(ões)
maior_pontuacao = times[0][1]

print("\n--- CAMPEÃO(ÕES) ---")
for i in range(4):
    if times[i][1] == maior_pontuacao:
        print(f"{times[i][0]} com {times[i][1]} pontos")
