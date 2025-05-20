"""ENUNCIADO
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
vetor1 = [i for i in range(1, 11)]
vetor2 = [i for i in range(11, 21)]

print(f"Vetor 1:", vetor1)
print(f"Vetor 2: ", vetor2)

vetor3 = []
for i in range(len(vetor1)):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(f" Vetor 3, feito com os valores compostos pelo vetor 1 e vetor 2 intercalados:")
print(f"O vetor 3 é: {vetor3}")





#help("__main__")