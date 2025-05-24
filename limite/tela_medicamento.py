class TelaMedicamento():
    def tela_opcoes(self):
        while True:
            try:
                print("-------- Medicamentos --------")
                print("1 - Registrar Medicamento")
                print("2 - Alterar ou Excluir Medicamento")
                print("3 - Listar Medicamentos")
                print("0 - Retornar")
                opcao = int(input("Escolha uma opção: "))
                if opcao in [0, 1, 2, 3]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número entre 0 e 3.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

    def pega_dados_medicamento(self):
        print("-------- Dados Medicamento --------")
        nome = input("Nome: ")
        fabricante = input("Fabricante: ")

        while True:
            try:
                preco = float(input("Preço (0 para cancelar): "))
                if preco == 0:
                    return None 
                return {"nome": nome, "fabricante": fabricante, "preco": preco}
            except ValueError:
                print("Preço inválido. Por favor, digite um número real ou cancele a operação ('0' para cancelar).")


    def mostra_medicamento(self, dados_medicamento):
        print("Nome: ", dados_medicamento["nome"])
        print("Fabricante: ", dados_medicamento["fabricante"])
        print("Preço: ", dados_medicamento["preco"])
        print("\n")

    def pede_nome_medicamento(self):
        return input("Digite o nome do medicamento: ")

    def mostra_opcoes_medicamentos(self, lista_medicamentos):
        print("Vários medicamentos encontrados com esse nome:")
        for idx, med in enumerate(lista_medicamentos, start=1):
            print(f"{idx} - Fabricante: {med.fabricante}")

    def pede_opcao_medicamento(self, total_opcoes):
        while True:
            try:
                opcao = int(input("Digite o número do medicamento desejado: "))
                if 1 <= opcao <= total_opcoes:
                    return opcao
                else:
                    print("Número fora do intervalo.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def mostra_opcoes_de_acao(self):
        print("O que deseja fazer com o medicamento selecionado?")
        print("1 - Alterar medicamento")
        print("2 - Excluir medicamento")
        print("0 - Cancelar")
        try:
            return int(input("Escolha a opção: "))
        except ValueError:
            print("Entrada inválida.")
            return -1

    def mostra_msg(self, msg):
        print(msg)
