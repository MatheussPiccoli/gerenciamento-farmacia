from datetime import datetime

class TelaEstoque():

    def tela_opcoes(self):
        while True:
            try:
                print("------ Estoque ------")
                print("1 - Listar Estoque")
                print("2 - Aumentar Estoque (Adicionar Lote)")
                print("3 - Baixar Estoque")
                print("4 - Verificar Estoque Baixo")
                print("5 - Listar Lotes Vencidos")
                print("6 - Listar Lotes Próximos ao Vencimento")
                print("0 - Retornar")
                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4, 5, 6]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número entre 0 e 6.")
            except ValueError:
                print("Opção inválida. Digite um número inteiro.")

    def pega_dados_lote(self):
        try:
            lote_str = input("Número do Lote: ")
            validade_str = input("Validade do lote (DD/MM/AAAA): ")
            validade = datetime.strptime(validade_str, "%d/%m/%Y").date()
            quantidade = int(input("Quantidade: "))
            return {"lote": lote_str, "validade": validade, "quantidade": quantidade}
        except ValueError:
            self.mostra_mensagem("Dados do lote inválidos. Verifique o formato da validade e da quantidade.")
            return None

    def pega_quantidade_para_baixa(self):
        try:
            return int(input("Quantidade para baixar do estoque: "))
        except ValueError:
            self.mostra_mensagem("Quantidade inválida. Por favor, digite um número inteiro.")
            return -1 

    def mostra_estoque(self, lotes):
        if not lotes:
            print("Nenhum lote no estoque.")
            return
        for lote_obj in lotes: 
            print(f"Medicamento: {lote_obj.medicamento.nome} | Lote: {lote_obj.lote} | Validade: {lote_obj.validade} | Quantidade: {lote_obj.quantidade}")

    def mostra_lote(self, lote):
        print(f"Lote → Medicamento: {lote.medicamento.nome} | Número do Lote: {lote.lote} | Validade: {lote.validade} | Quantidade: {lote.quantidade}")

    def mostra_mensagem(self, msg):
        print(msg)