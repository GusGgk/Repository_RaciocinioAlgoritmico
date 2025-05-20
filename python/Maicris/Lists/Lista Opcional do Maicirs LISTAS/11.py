"""ENUNCIADO
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.(programa 10.py)"""
vetor1 = [i for i in range(1,11)]
vetor2 = [i for i in range(11,21)]
vetor3 = [i for i in range(21,31)]
vetor_geral = []

print(f"Valores do vetor 1: ",vetor1)
print(f"Valores do vetor 2:",vetor2)
print(f"Valores do vetor 3:",vetor3)

for i in range(len(vetor1)):
    vetor_geral.append(vetor1[i])
    vetor_geral.append(vetor2[i])
    vetor_geral.append(vetor3[i])
print("Os 3 vetores intercalados ficam assim:")
print(vetor_geral)

#help("__main__")