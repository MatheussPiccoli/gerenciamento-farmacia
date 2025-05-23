from limite.tela_estoque import TelaEstoque
from Models.medicamento import Medicamento
from Models.lote import LoteMedicamento
from Models.estoque import Estoque
from controle.exceptions import DadoInvalidoException, EstoqueInsuficiente, EstoqueVazio


class ControladorEstoque:
    def __init__(self, controlador_sistema):
        self.__estoque = Estoque()
        self.__controlador_sistema = controlador_sistema
        self.__tela_estoque = TelaEstoque()

    def listar_estoque(self):
        lotes = self.__estoque.lotes
        self.__tela_estoque.mostra_estoque(lotes)
        if not lotes:
            raise EstoqueVazio()
            return

    def atualizar_estoque(self):
        lista_opcoes = {1: self.aumentar_estoque, 2: self.abaixar_estoque,
                        0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_estoque.update_estoque]

    def aumentar_estoque(self):
        self.listar_estoque()
        dados = self.__tela_estoque.pega_dados()
        medicamento = dados["medicamento"]
        quantidade = dados["quantidade"]
        validade = dados["validade"]

        if not isinstance(medicamento, Medicamento) or quantidade <= 0:
            raise DadoInvalidoException()
            return
        
        lote_existente = None
        for lote in self._Estoque__lotes:
            if lote.medicamento == medicamento and lote.validade == validade:
                lote_existente = lote
                break
        
        if lote_existente:
            lote_existente.quantidade += quantidade
        else:
            novo_lote = LoteMedicamento(medicamento, quantidade, validade)
            self.__estoque.add_lote(novo_lote)
        
        self.__tela_estoque.mostra_mensagem("Estoque aumentado com sucesso")

    def abaixar_estoque(self):
        self.listar_estoque()
        dados = self.__tela_estoque.pega_dados()
        medicamento = dados["medicamento"]
        quantidade = dados["quantidade"]
        validade = dados["validade"]

        quantidade_disponivel = self.__estoque.consultar_estoque(medicamento)
        if quantidade_disponivel is None or quantidade_disponivel < quantidade:
            raise EstoqueInsuficiente()
            return
        
        self.__estoque.baixar_estoque(medicamento, quantidade)
        self.__tela_estoque.mostra_mensagem("Estoque diminuído com sucesso")

    def estoque_baixo(self):
        self.listar_estoque()
        lotes_baixos = self.__estoque.estoque_baixo()
        for item in self.__estoque.lotes:
            if item.quantidade < 5:
                self.__tela_estoque.pouco_estoque(item)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.listar_estoque, 2: self.atualizar_estoque,
                        3: self.estoque_baixo, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_estoque.tela_opcoes()]()
