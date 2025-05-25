from datetime import datetime

class TelaLoteMedicamento:
    def tela_opcoes(self):
        while True:
            try:
                print("------ Lotes de Medicamento ------")
                print("1 - Listar lotes por medicamento")
                print("2 - Verificar lotes vencidos")
                print("3 - Verificar validade próxima")
                print("0 - Retornar")
                opcao = int(input("Escolha uma opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def pega_dados_lote(self):
        try:
            lote = input("Código do lote: ")
            validade = input("Data de validade (DD/MM/AAAA): ")
            quantidade = int(input("Quantidade: "))
            validade = datetime.strptime(validade, "%d/%m/%Y").date()
            return {"lote": lote, "validade": validade, "quantidade": quantidade}
        except ValueError:
            print("Dados inválidos. Tente novamente.")
            return None

    def mostra_lote(self, dados):
        print(f"Lote: {dados['lote']}, Validade: {dados['validade']}, Quantidade: {dados['quantidade']}")

    def mostra_msg(self, msg):
        print(msg)
