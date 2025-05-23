from limite.tela_venda import TelaVenda
from limite.tela_cliente import TelaCliente
from limite.tela_venda import TelaVenda
from Models.venda import Venda
from Models.itemvenda import ItemVenda
from controle.controlador_cliente import Controladorclientes
from controle.controlador_estoque import ControladorEstoque
from controle.exceptions import MedicamentoNaoEncontrado, VendaNaoExistente, EstoqueInsuficiente, ClienteNaoEncontrado
from datetime import datetime, date


class ControladorVenda:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_venda = TelaVenda()
        self.__tela_cliente = TelaCliente()
        self.__tela_venda = TelaVenda()
        self.__vendas = []

    def registrar_venda(self):
        itens = []
        while True:
            produtos = self.__controlador_sistema.controlador_estoque.listar_estoque()
            self.__tela_venda.mostra_produtos(produtos)
            dados_item = self.pega_dados_item()

            medicamento = self.__controlador_sistema.controlador_estoque.pega_medicamento_por_nome(dados_item["nome"])
            if not medicamento:
                raise MedicamentoNaoEncontrado()
                continue
            if not medicamento.verifica_quantidade(dados_item["quantidade"]):
                raise EstoqueInsuficiente()
                continue

            valor_unitario = medicamento.preco
            item = ItemVenda(dados_item["nome"], dados_item["fabricante"], valor_unitario,
                              dados_item["quantidade"], dados_item["id"])
            item.calcular_subtotal()
            itens.append(item)
            self.__controlador_sistema.controlador_estoque.abaixar_estoque(dados_item["nome"], dados_item["quantidade"])

            if not self.__tela_venda.continuar_venda():
                break
        
        if not itens:
            self.__tela_venda.mostra_mensagem("Nenhum item adicionado à venda.")
            return

        self.listar_vendas()
        id_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_por_id(id_venda)        
        if not venda:
            raise VendaNaoExistente()
            return
        
        self.__controlador_sistema.controlador_cliente.lista_clientes()
        id_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_por_id(id_cliente)        
        if not cliente:
            raise ClienteNaoEncontrado()
            return
        
        venda = Venda(venda, cliente, itens, date.today())
        for item in itens:
            venda.adicionar_item(item)
        total_venda = venda.valor_total()
        self.__vendas.append(venda)
        self.__tela_venda.mostra_mensagem("Venda registrada com sucesso! Total: R$ {total:.2f}")
    
    def pega_dados_item(self):
        dados_item = self.__tela_venda.pega_dados_item()
        item = ItemVenda(dados_item["nome"], dados_item["fabricante"], 
                         dados_item["preço"], dados_item["quantidade"],
                         dados_item["id"])
        item.calcular_subtotal()
        return item
    
    def continuar_adicionando(self):
        lista_opcoes = {1: self.continuar_adicionando, 2: self.registrar_venda}

        while True:
            opcao = self.__tela_venda.continuar_venda()
            funcao_escolhida = lista_opcoes[opcao]
            if opcao == 1:
                return True

    def adicionar_item(self, item : ItemVenda):
        if isinstance(item, ItemVenda):
            self.__itens.append(item)
    
    def valor_total(self):
        self.__valor_total = sum(item.subtotal for item in self.__itens)
        return self.__valor_total

    def alterar_venda(self):
        self.listar_vendas()
        id_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_por_id(id_venda)

        if venda is not None:
            novos_dados_venda = self.__tela_venda.pega_dados_venda()
            venda.cliente = novos_dados_venda["cliente"]
            venda.farmaceutico = novos_dados_venda["farmaceutico"]
            venda.medicamento = novos_dados_venda["medicamento"]
            venda.quantidade = novos_dados_venda["quantidade"]
            self.listar_vendas()
        else:
            raise VendaNaoExistente()

    def pega_venda_por_id(self, id: int):
        for venda in self.__vendas:
            if(venda.id == id):
                return venda
        return None

    def listar_vendas(self):
        for venda in self.__vendas:
            self.__tela_venda.mostra_venda({"id": venda.id, "cliente": venda.cliente.nome, 
                                            "farmaceutico": venda.farmaceutico.nome, 
                                            "data": venda.data, "itens": venda.itens})
        

    def excluir_venda(self):
        self.listar_vendas()
        id_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_por_id(id_venda)
        if venda is not None:
            self.__vendas.remove(venda)
            self.listar_vendas()
        else:
            raise VendaNaoExistente()


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.registrar_venda, 2: self.alterar_venda, 3: self.listar_vendas,
                         4: self.excluir_venda, 5: self.pega_venda_por_id, 0: self.retornar}
               
        continua = True
        while continua:
            lista_opcoes[self.__tela_venda.tela_opcoes()]()
