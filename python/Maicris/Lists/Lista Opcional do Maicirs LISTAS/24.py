"""ENUNCIADO
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em
um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma
função para gerar numeros aleatórios, simulando os lançamentos dos dados."""

import random

resultados = [] 
contadores = [0, 0, 0, 0, 0, 0]  

# Simulando 100 lançamentos
for i in range(100):
    numero = random.randint(1, 6)  # sorteia número entre 1 e 6
    resultados.append(numero)
    contadores[numero - 1] += 1  


print("Resultado dos lançamentos:")
for i in range(6):
    print(f"O número {i+1} apareceu {contadores[i]} vezes.")
