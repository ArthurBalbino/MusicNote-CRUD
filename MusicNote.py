musica1 = ""
opcao = 0


while opcao != 5:
    print("\n-Music Note-")
    print("1 - Cadastrar Música")
    print("2 - Consultar Música")
    print("3 - Editar Música")
    print("4 - Excluir música")
    print("5 - Sair")

    opcao = int(input("escolha uma opção: "))

    if opcao == 1:
        musica1 = input("escreva sua música: ")
        print("música cadastrada!")

    elif opcao == 2:
        if musica1 != "":
            print("Sua música: ", musica1)
        else: 
            print("nenhuma música cadastrada.")

    elif opcao == 3:
        if musica1 != "":
            musica1 = input("Digite a nova música: ")
            print("Música editada!")
        else:
            print("Não existe música para editar.")

    elif opcao == 4:
        if musica1 != "":
            musica1 = ""
            print("Música excluída!")
        else:
            print("Não existe música para excluir.")

    elif opcao == 5:
        print("Saindo do MusicNote...")

    else:
        print("Opção inválida!")