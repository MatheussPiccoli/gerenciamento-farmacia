from datetime import datetime, date

class TelaRelatorios():
    def tela_opcoes(self):
        while True:
            try:
                print("-------- Relatórios --------")
                print("1 - Vendas por Período")
                print("2 - Medicamentos mais Vendidos")
                print("3 - CLientes que mais Compraram")
                print("4 - Melhores Vendedores")
                print("0 - Retornar")

                opcao = int(input("Escolha uma opção: "))
                if opcao in [0, 1, 2, 3]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número entre 0 e 3.")
            
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

    def pega_periodo(self):
        while True:
            try:
                data_inicio = input("Data de início (dd/mm/aaaa): ")
                data_fim = input("Data de fim (dd/mm/aaaa): ")

                data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y").date()
                data_fim = datetime.strptime(data_fim, "%d/%m/%Y").date()

                if data_inicio > data_fim:
                    print("A data de início não pode ser maior que a data de fim.")
                    continue

                return data_inicio, data_fim
            
            except ValueError:
                print("Formato de data inválido. Por favor, use o formato dd/mm/aaaa.")

    def mostra_venda(self, dados_venda):
        print("Cliente: ", dados_venda["cliente"])
        print("Farmacêutico: ", dados_venda["farmaceutico"])
        print("Data: ", dados_venda["data"])
        print("Itens da Venda:")
        if dados_venda["itens"]: 
            for item in dados_venda["itens"]:
                print(f"  - Medicamento: {item.medicamento.nome} | Quantidade: {item.quantidade} | Subtotal: R$ {item.subtotal:.2f}")
        else:
            print("  Nenhum item registrado para esta venda.")
        
        print("\n")

    def mostra_msg(self, msg):
        print(msg)

        