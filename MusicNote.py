
musicas = []
opcao = 0

while opcao != 5:
    print("\n  --- MUSICNOTE ---")
    print("1 - Cadastrar música")
    print("2 - Consultar músicas")
    print("3 - Editar música")
    print("4 - Excluir música")
    print("5 - Sair")

    entrada = input("Escolha uma opção: ")

    if not entrada.isdigit():
        print("Digite apenas o número de cada opção.")
        continue

    opcao = int(entrada)

    if opcao == 1:
        print("\n--- CADASTRAR MÚSICA ---")

        titulo = input("Título: ")
        artista = input("Artista: ")
        tom = input("Tom musical: ")
        cifra = input("Cifra: ")

        if titulo != "":
            musica = {
                "titulo": titulo,
                "artista": artista,
                "tom": tom,
                "cifra": cifra
            }

            musicas.append(musica)
            print("Música cadastrada com sucesso!")
        else:
            print("O título não pode ficar vazio.")

    elif opcao == 2:
        print("\n--- CONSULTAR MÚSICAS ---")

        if len(musicas) == 0:
            print("Nenhuma música cadastrada.")
        else:
            for i in range(len(musicas)):
                print(i + 1, "-", musicas[i]["titulo"])

            escolha = input(
                "Número da música para ver detalhes: "
            )

            if escolha.isdigit():
                indice = int(escolha) - 1

                if indice >= 0 and indice < len(musicas):
                    musica = musicas[indice]

                    print("Título:", musica["titulo"])
                    print("Artista:", musica["artista"])
                    print("Tom:", musica["tom"])
                    print("Cifra:", musica["cifra"])
                else:
                    print("Música não encontrada.")
            else:
                print("Digite um número válido.")

    elif opcao == 3:
        print("\n--- EDITAR MÚSICA ---")

        if len(musicas) == 0:
            print("Nenhuma música para editar.")
        else:
            for i in range(len(musicas)):
                print(i + 1, "-", musicas[i]["titulo"])

            escolha = input(
                "Número da música para editar: "
            )

            if escolha.isdigit():
                indice = int(escolha) - 1

                if indice >= 0 and indice < len(musicas):
                    novo_titulo = input("Novo título: ")
                    novo_artista = input("Novo artista: ")
                    novo_tom = input("Novo tom: ")
                    nova_cifra = input("Nova cifra: ")

                    if novo_titulo != "":
                        musicas[indice]["titulo"] = novo_titulo
                        musicas[indice]["artista"] = novo_artista
                        musicas[indice]["tom"] = novo_tom
                        musicas[indice]["cifra"] = nova_cifra

                        print("Música editada com sucesso!")
                    else:
                        print("Edição cancelada: título vazio.")
                else:
                    print("Música não encontrada.")
            else:
                print("Digite um número válido.")

    elif opcao == 4:
        print("\n--- EXCLUIR MÚSICA ---")

        if len(musicas) == 0:
            print("Nenhuma música para excluir.")
        else:
            for i in range(len(musicas)):
                print(i + 1, "-", musicas[i]["titulo"])

            escolha = input(
                "Número da música para excluir: "
            )

            if escolha.isdigit():
                indice = int(escolha) - 1

                if indice >= 0 and indice < len(musicas):
                    confirmar = input(
                        "Confirmar exclusão? (s/n): "
                    )

                    if confirmar == "s":
                        musicas.pop(indice)
                        print("Música excluída com sucesso!")
                    else:
                        print("Exclusão cancelada.")
                else:
                    print("Música não encontrada.")
            else:
                print("Digite um número válido.")

    elif opcao == 5:
        print("Saindo do MusicNote...")

    else:
        print("Opção inválida.")
