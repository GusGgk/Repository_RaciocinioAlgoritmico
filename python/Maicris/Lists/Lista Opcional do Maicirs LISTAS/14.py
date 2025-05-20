"""ENUNCIADO
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente"."""


Respostas_do_usuario = []
perguntas =["A. Telefonou para a vítima? (S/N): ",
            "B. Esteve no local do Crime? (S/N): ",
            "C. Mora perto da vítima? (S/N): ",
            "D. Devia para a vitíma? (S/N): ",
            "E. Já trabalhou com a vitíma? (S/N): "]

print("--- INTERROGATÓRIO ---")
print(f"\n Responta S para sim e N para não...")

for i in range(5):
   print(perguntas[i])
   resposta = input("S ou N?").lower()
   Respostas_do_usuario.append(resposta)
print(Respostas_do_usuario)

print(f"\n--- CLASSIFICAÇÃO DO CRIME ---")
respostas_positivas = Respostas_do_usuario.count("s")
print(f"Das 5 perguntas ele respondeu sim para: {respostas_positivas} ")

if respostas_positivas == 2:
   print(f"\n ---Esta pessoa é SUSPEITA! ---")
elif 3 <= respostas_positivas <= 4:
   print(f"\n ---Esta pessoa é CÚMPLICE! ---")
elif respostas_positivas == 5:
   print(f"\n --- Esta pessoa é a ASSASSINA! ---")
else:
   print(f"\n --- Essa pessoa é INOCENTE! ---")
   
   #help("__main__")