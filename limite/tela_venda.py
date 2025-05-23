from Models.venda import Venda
from Models.itemvenda import ItemVenda


class TelaVenda():
    def tela_opcoes(self):
        print("-------- Vendas ----------")
        print("Escolha a opção")
        print("1 - Registrar venda")
        print("2 - Alterar venda")
        print("3 - Listar vendas")
        print("4 - Excluir venda")
        print("5 - Buscar venda")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def seleciona_venda(self):
        id_venda = int(input("ID da venda que deseja selecionar: "))
        return id_venda

    def pega_dados_venda(self):
        print("-------- Dados Venda ----------")
        nome_cliente = input("Nome do cliente: ")
        nome_farmaceutico = input("Nome do farmaceutico: ")
        medicamento = input("Medicamento: ")
        quantidade = int(input("Quantidade: "))

    def pega_dados_item(self):
        print("-------- Dados Item Venda ----------")
        nome_medicamento = input("Nome do medicamento: ")
        fabricante = input("Fabricante: ")
        valor_unitario = float(input("Valor unitario: "))
        quantidade = int(input("Quantidade: "))
        id_item = ItemVenda.contador_id
        return {"nome": nome_medicamento, "fabricante": fabricante, "preco": valor_unitario,
                "quantidade": quantidade, "id": id_item}

    def continuar_venda(self):
        print("Deseja adicionar mais produtos a venda?")
        print("1 - Sim")
        print("2 - Não")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def mostra_venda(self, dados_venda):
        print("ID da venda: ", dados_venda["id"])
        print("ID do cliente: ", dados_venda["id_cliente"])
        print("ID do venda: ", dados_venda["id_venda"])
        print("Data da venda: ", dados_venda["data"])

        opcao = int(input("Escolha a opção: "))
        return opcao

    def mostra_produtos(self):
        for item in self.__itens:
            print(f"ID: {item.id}, Medicamento: {item.nome_medicamento}, Fabricante: {item.fabricante}, "
                  f"Valor Unitario: {item.preco}, Quantidade: {item.quantidade}")

    def mostra_mensagem(self, msg):
        print(msg)
