from Models.estoque import Estoque


class TelaEstoque:
    def tela_opcoes(self):
        print("-------- Estoque ----------")
        print("1 - Visualizar estoque")
        print("2 - Atualizar estoque")
        print("3 - Ver estoques baixos")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def update_estoque(self):
        print("-------- Atualizar estoque --------")
        print("1 - Aumentar")
        print("2 - Baixar")
        print("0 - Retornar")

        opcao = int(input("Ecolha a opção: "))

    def pega_dados(self):
        print("-------- Dados do produto --------")
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        validade = input("Validade: ")

        return {"nome": nome, "quantidade": quantidade, "validade": validade}
    
    def mostra_estoque(self, dados_estoque):
        print("Nome do produto: ", dados_estoque["nome"])
        print("Quantidade do produto: ", dados_estoque["quantidade"])
        print("Validade do produto: ", dados_estoque["validade"])
        print("\n")

    def pouco_estoque(self, dados_estoque):
        print("-------- Estoque baixo --------")
        print("Nome do produto: ", dados_estoque["nome"])
        print("Quantidade do produto: ", dados_estoque["quantidade"])
        print("Validade do produto: ", dados_estoque["validade"])
        print("\n")
