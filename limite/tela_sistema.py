class TelaSistema:
    def tela_opcoes(self):
        print("-------- Sistema ---------")
        print("Escolha sua opção")
        print("1 - Clientes")
        print("2 - Farmaceuticos")
        print("3 - Venda")
        print("4 - Estoque")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opção:"))
        return opcao