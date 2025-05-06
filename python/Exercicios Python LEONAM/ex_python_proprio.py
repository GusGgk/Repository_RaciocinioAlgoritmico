def gerenciador_De_tarefas():
    tarefas = []
 
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Listar tarefas")
        print("4. Sair")         
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome_da_tarefa = input("Digite o Nome da tarefa: ")
            descricao_tarefa = input("Digite a descrição da tarefa: ")
            
            pass
        elif opcao == "2":
            #adicionar a logica
            pass
        elif opcao == "3":
            #adicionar a logica
            pass
        elif opcao == "4":
            print("Saindo do gerenciador de tarefas.")
            break  # Sai do loop while e encerra o programa
        else:
            print("Opção inválida, tente novamente!")

gerenciador_De_tarefas()