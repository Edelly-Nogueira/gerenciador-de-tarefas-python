# ==========================================
# GERENCIADOR DE TAREFAS - PROJETO 2
# ==========================================

# Lista onde todas as tarefas serão armazenadas
tarefas = []

# Controla se o programa continua rodando
programa_ativo = True


# ==========================================
# MENU PRINCIPAL
# ==========================================

while programa_ativo:

    print("\n" + "=" * 40)
    print("      GERENCIADOR DE TAREFAS")
    print("=" * 40)

    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Excluir tarefa")
    print("5 - Salvar e sair")

    opcao = input("\nEscolha uma opção: ")


    # ======================================
    # OPÇÃO 1 - ADICIONAR TAREFA
    # ======================================

    if opcao == "1":

        nome_tarefa = input("\nDigite o nome da tarefa que deseja adicionar: ")
        prazo_tarefa = input("Digite o prazo da tarefa (dd/mm/aaaa): ")

        nova_tarefa = {
            "nome": nome_tarefa,
            "prazo": prazo_tarefa,
            "status": "pendente"
        }

        tarefas.append(nova_tarefa)

        print("\nTarefa adicionada com sucesso!")


    # ======================================
    # OPÇÃO 2 - LISTAR TAREFAS
    # ======================================

    elif opcao == "2":

        print("\n=== LISTA DE TAREFAS ===\n")

        for numero, tarefa in enumerate(tarefas, start=1):

            if tarefa["status"] == "pendente":
                simbolo = "[ ]"
            else:
                simbolo = "[x]"

            print(f"{numero} - {simbolo} {tarefa['nome']} - Prazo: {tarefa['prazo']}")


    # ======================================
    # OPÇÃO 3 - MARCAR COMO CONCLUÍDA
    # ======================================

    elif opcao == "3":

        print("\n=== MARCAR TAREFA COMO CONCLUÍDA ===")
        print("=== LISTA DE TAREFAS ===\n")

        for numero, tarefa in enumerate(tarefas, start=1):

            if tarefa["status"] == "pendente":
                simbolo = "[ ]"
            else:
                simbolo = "[x]"

            print(f"{numero} - {simbolo} {tarefa['nome']} - Prazo: {tarefa['prazo']}")

        escolha_tarefa = int(input("\nDigite o número da tarefa que deseja marcar como concluída: "))

        indice = escolha_tarefa - 1
        tarefas[indice]["status"] = "concluída"

        print("\nA tarefa foi marcada como concluída com sucesso!")


    # ======================================
    # OPÇÃO 4 - EXCLUIR TAREFA
    # ======================================

    elif opcao == "4":

        print("\n=== EXCLUIR TAREFA ===")
        print("=== LISTA DE TAREFAS ===\n")

        for numero, tarefa in enumerate(tarefas, start=1):

            if tarefa["status"] == "pendente":
                simbolo = "[ ]"
            else:
                simbolo = "[x]"

            print(f"{numero} - {simbolo} {tarefa['nome']} - Prazo: {tarefa['prazo']}")

        escolha_tarefa = int(input("\nDigite o número da tarefa que deseja excluir: "))

        indice = escolha_tarefa - 1
        tarefas.pop(indice)

        print("\nTarefa excluída com sucesso!")


    # ====================================
    # OPÇÃO 5 - SALVAR E SAIR
    # ====================================

    elif opcao == "5":

        with open("tarefas.txt", "w", encoding="utf-8") as arquivo:

            for tarefa in tarefas:
                arquivo.write(
                    f"{tarefa['nome']} - Prazo: {tarefa['prazo']} - Status: {tarefa['status']}\n"
                )

        programa_ativo = False

        print("\nTarefas salvas com sucesso em tarefas.txt.")
        print("Programa encerrado.")


    # ====================================
    # OPÇÃO INVÁLIDA
    # ====================================

    else:

        print("\nOpção inválida. Tente novamente.")