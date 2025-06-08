def guardar_numeros():
    lista = []
    while True:
        entrada = input("Digite um numero(para sair digite 'sair'): ").lower()
        if entrada == "sair":
            break
        lista.append(float(entrada))
    return lista

def calcular_media(numeros):
    return sum(numeros) / len(numeros)


numeros = guardar_numeros()
media = calcular_media(numeros)

print(f"A lista de números é: {numeros} e a média deles é: {media:.2f}")