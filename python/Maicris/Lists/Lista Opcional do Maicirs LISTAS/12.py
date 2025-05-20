"""ENUNCIADO
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
13 anos possuem altura inferior à média de altura desses alunos."""

alunos = [i for i in range(1,31)]

idades = [12, 14, 11, 15, 16, 18, 11, 11, 13, 15, 
          16, 16, 17, 14, 13, 12, 14, 15, 16, 17, 
          13, 14, 15, 16, 17, 18, 12, 13, 14, 15]


alturas = [150, 160, 145, 158, 165, 170, 142, 148, 152, 160, 
           167, 169, 172, 159, 154, 151, 157, 161, 168, 174, 
           153, 158, 162, 169, 173, 175, 149, 155, 159, 163]


for i in range(30):
    print(f"O Aluno {alunos[i]} tem a idade de: {idades[i]} e a altura de: {alturas[i]}")
    

media_altura = sum(alturas) / len(alturas)
print(f"A Média de alturas dos alunos são: {media_altura:.2f}")

contador = 0

for i in range(30): 
    if idades[i] > 13 and alturas[i] < media_altura:
        contador += 1

print(f"Número de alunos com mais de 13 anos e altura inferior à média: {contador}")

#help("__main__")