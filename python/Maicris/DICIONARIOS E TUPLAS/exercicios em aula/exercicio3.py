"""Enunciado
3. Criar um programa que cadastre locais históricos do mundo com
suas coordenadas fazendo uso de tuplas com parâmetros
nomeados. Dica: usar a função namedtuple(). """
from collections import namedtuple

locais_historicos = []

local = namedtuple("Local",["nome","latitude","longitude"])

while True:
    nome = input("Qual o nome do local? ")
    if nome == "0":
        break
    lat = float(input("Qual a latitude do local? "))
    lon = float(input("Qual a longitude do local? "))

    lugar = local(nome, lat, lon)
    locais_historicos.append(lugar)

for pos, lugar in enumerate(locais_historicos):
    print(f"\n--- Local {pos+1} ---")
    print(f"Nome: {lugar.nome}")
    print(f"Latitude: {lugar.latitude}")
    print(f"Longitude: {lugar.longitude}")

        