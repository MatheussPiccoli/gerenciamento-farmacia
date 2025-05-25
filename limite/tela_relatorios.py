import datetime

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
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    print("Opção inválida. Digite um número entre 0 e 4.")
            
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

    def pega_periodo(self):
        while True:
            try:
                data_inicio = input("Data de início (dd/mm/aaaa): ")
                data_fim = input("Data de fim (dd/mm/aaaa): ")

                # Converte as strings para objetos datetime
                data_inicio = datetime.datetime.strptime(data_inicio, "%d/%m/%Y")
                data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")

                if data_inicio > data_fim:
                    print("A data de início não pode ser maior que a data de fim.")
                    continue

                return data_inicio, data_fim
            
            except ValueError:
                print("Formato de data inválido. Por favor, use o formato dd/mm/aaaa.")