"""Enunciado
2. Criar um programa que cadastre funcionário de uma empresa e
seus dependentes. O funcionário deve ser cadastrado com
matrícula, nome e dependentes. Os dependentes devem ser
inseridos dinamicamente em uma tupla. Dica: usar o operador
+=."""

cadastro = []


while True:
    matricula = input("Digite o número da matrícula(não digite nada para sair): ")
    if matricula == "":
        break
    nome = input("Digite o nome do funcionário: ")
    tupla_dependente = tuple()
    
    while True:
        dependente = input("O usuário possui dependentes(s/n)?").lower()
        if dependente == "n":
            tupla_dependente += ("Não possui Dependentes",)
            dicionario = {"n° da Matricula": matricula, "nome": nome, "Dependentes": tupla_dependente}
            break
        
 
        elif dependente == "s":
            quantidade_dependentes = int(input("Possui quantos dependentes? "))
            if quantidade_dependentes >= 2:
                for i in range(quantidade_dependentes):
                    nome_dependente = input("Digite o nome do seu dependente: ")
                    tupla_dependente += (nome_dependente,)
                    dicionario = {"n° da Matricula": matricula, "nome": nome, "Dependentes": tupla_dependente}
                break
                    
            else:
                nome_dependente = input("Digite o nome do seu dependente: ") 
                tupla_dependente += (nome_dependente,)
                dicionario = {"n° da Matricula": matricula, "nome": nome, "Dependentes": tupla_dependente}
                break
                   
        else:
            print("Informe s(sim) ou n(não)...")    
    cadastro.append(dicionario)               
        
      
for pos, dicionario in enumerate(cadastro):
    print(f"\n---- Usuário {pos+1} ----")
    for key, value in dicionario.items():
        print(f"{key}: {value}")                
            
    
    

        
