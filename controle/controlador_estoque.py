from datetime import date
from limite.tela_estoque import TelaEstoque
from Models.medicamento import Medicamento
from Models.estoque import Estoque
from controle.exceptions import DadoInvalidoException, EstoqueInsuficiente, EstoqueVazio, MedicamentoNaoEncontrado
from datetime import datetime
from DAOs.estoque_dao import EstoqueDAO

class ControladorEstoque:
    def __init__(self, controlador_sistema):
        self.__estoque_dao = EstoqueDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_estoque = TelaEstoque()

    def listar_estoque(self):
        estoque = self.__estoque_dao.get_estoque()
        if estoque is None:
            self.__tela_estoque.mostra_mensagem("Estoque não inicializado.")
            return
        lotes = estoque.lotes
        if not lotes:
            self.__tela_estoque.mostra_mensagem("Estoque vazio.")
            return
        dados_lotes = []
        for lote in lotes:
            dados_lotes.append({
                "id": lote.medicamento.id,
                "nome": lote.medicamento.nome,
                "lote": lote.lote,
                "validade": lote.validade,
                "quantidade": lote.quantidade
            })
        self.__tela_estoque.mostra_estoque(dados_lotes)

    def aumentar_estoque(self):
        try:
            medicamento = self.__controlador_sistema.controlador_medicamento.seleciona_medicamento()
            if not medicamento: 
                self.__tela_estoque.mostra_mensagem("Nenhum medicamento selecionado.")
                return
        except MedicamentoNaoEncontrado:
            self.__tela_estoque.mostra_mensagem("Medicamento não encontrado.")
            return
        dados = self.__tela_estoque.pega_dados_lote()
        if dados is None: 
            return
        if dados["quantidade"] <= 0:
            self.__tela_estoque.mostra_mensagem("A quantidade deve ser maior que zero.")
            return 
        estoque = self.__estoque_dao.get_estoque()
        if estoque is None:
            self.__tela_estoque.mostra_mensagem("Estoque não inicializado.")
            return
        estoque.adicionar_lote(
            medicamento=medicamento,
            lote=dados["lote"],
            validade=dados["validade"],
            quantidade=dados["quantidade"]
        )
        self.__estoque_dao.update(estoque)
        self.__tela_estoque.mostra_mensagem("Lote adicionado ao estoque com sucesso.")

    def abaixar_estoque(self):
        try:
            medicamento = self.__controlador_sistema.controlador_medicamento.seleciona_medicamento()
            if not medicamento:
                self.__tela_estoque.mostra_mensagem("Nenhum medicamento selecionado.")
                return
        except MedicamentoNaoEncontrado:
            self.__tela_estoque.mostra_mensagem("Medicamento não encontrado.")
            return
        quantidade = self.__tela_estoque.pega_quantidade_para_baixa()
        if quantidade is None or quantidade < 0:
            self.__tela_estoque.mostra_mensagem("Quantidade para baixa deve ser um número positivo.")
            return
        estoque = self.__estoque_dao.get_estoque()
        if estoque is None:
            self.__tela_estoque.mostra_mensagem("Estoque não inicializado.")
            return
        try:
            estoque.abaixar_estoque(medicamento, quantidade)
            self.__estoque_dao.update(estoque)
            self.__tela_estoque.mostra_mensagem("Estoque baixado com sucesso.")
        except EstoqueInsuficiente:
            self.__tela_estoque.mostra_mensagem("Estoque insuficiente para a quantidade solicitada.")
        except ValueError:
            self.__tela_estoque.mostra_mensagem("Quantidade inválida.")

    def estoque_baixo(self):
        estoque = self.__estoque_dao.get_estoque()
        if estoque is None:
            self.__tela_estoque.mostra_mensagem("Estoque não inicializado.")
            return
        lotes_baixos = estoque.estoque_baixo(limite=5)
        self.__tela_estoque.mostra_estoque_baixo(lotes_baixos)

    def consultar_total_medicamento(self, medicamento: Medicamento) -> int:
        estoque = self.__estoque_dao.get_estoque()
        if estoque is None:
            self.__tela_estoque.mostra_mensagem("Estoque não inicializado.")
            return 0
        return estoque.consultar_estoque(medicamento)
    
    def realizar_baixa_medicamento(self, medicamento: Medicamento, quantidade: int): 
        if not isinstance(medicamento, Medicamento):
            raise TypeError("O argumento 'medicamento' deve ser uma instância de Medicamento.")
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("A quantidade deve ser um número inteiro positivo.")
            
        estoque = self.__estoque_dao.get_estoque()
        if estoque is None:
            self.__tela_estoque.mostra_mensagem("Estoque não inicializado.")
            return
        estoque.abaixar_estoque(medicamento, quantidade)
        self.__estoque_dao.update(estoque)

    def lotes_vencidos(self):
        estoque = self.__estoque_dao.get_estoque()
        if estoque is None:
            self.__tela_estoque.mostra_mensagem("Estoque não inicializado.")
            return
        lotes_vencidos = estoque.lotes_vencidos()
        self.__tela_estoque.mostra_lotes_vencidos(lotes_vencidos)

    def lotes_proximos_vencimento(self):
        estoque = self.__estoque_dao.get_estoque()
        if estoque is None:
            self.__tela_estoque.mostra_mensagem("Estoque não inicializado.")
            return
        lotes_proximos = estoque.lotes_proximos_vencimento(dias_limite=30)
        self.__tela_estoque.mostra_lotes_proximos(lotes_proximos)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.listar_estoque,
            2: self.aumentar_estoque,
            3: self.abaixar_estoque,
            4: self.estoque_baixo,
            5: self.lotes_vencidos,
            6: self.lotes_proximos_vencimento,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_estoque.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
