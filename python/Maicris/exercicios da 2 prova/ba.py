"""Cadastrar o usuario , deu um modelo de exemplo, era um dicionario, ai dentro dele tinha um dicionario como valor e uma lista como valor do valor (tudo alinhado)"""
""""Era um dicionário onde o valor era outro dicionário, e dentro desse segundo dicionário havia uma lista como um dos valores."""

usuarios = {}


cpf = input("Digite o CPF: ")
nome = input("Digite o Nome: ")
idade = int(input("Digite a Idade: "))

cursos = []
while True:
    curso = input("Digite um curso (0 para parar): ")
    if curso == "0":
        break
    cursos.append(curso)

usuario = {
    "nome":nome,
    "idade": idade,
    "cursos": cursos
}

usuarios[cpf] = usuario

print("\n*** USUÁRIOS CADASTRADOS ***\n")

for cpf, dados in usuarios.items():
    print(f"CPF: {cpf}")
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados["idade"]}")
    print("Cursos:")
    for curso in dados["cursos"]:
        print(f" - {curso}")
    print("-" * 30)