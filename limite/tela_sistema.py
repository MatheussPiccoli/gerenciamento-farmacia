
class TelaSistema:
    def tela_opcoes(self):
        while True:
            try:
                print("-------- Sistema ---------")
                print("Escolha sua opção")
                print("1 - Clientes")
                print("2 - Farmaceuticos")
                print("3 - Venda")
                print("4 - Estoque")
                print("5 - Medicamentos")
                print("6 - Lotes")
                print("7 - Relatórios")
                print("0 - Finalizar sistema")
                opcao = int(input("Escolha a opção:"))
                if opcao in [0, 1, 2, 3, 4, 5, 6, 7]:
                    return opcao
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")