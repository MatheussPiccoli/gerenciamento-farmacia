# controle/controlador_estoque.py

from limite.tela_estoque import TelaEstoque
from Models.medicamento import Medicamento
from Models.estoque import Estoque
from controle.exceptions import DadoInvalidoException, EstoqueInsuficiente, EstoqueVazio, MedicamentoNaoEncontrado
from datetime import datetime

class ControladorEstoque:
    def __init__(self, controlador_sistema):
        self.__estoque = Estoque()
        self.__controlador_sistema = controlador_sistema
        self.__tela_estoque = TelaEstoque()

    def listar_estoque(self):
        lotes = self.__estoque.lotes
        if not lotes:
            self.__tela_estoque.mostra_mensagem("Estoque vazio.")
            return

        self.__tela_estoque.mostra_estoque(lotes)

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

        self.__estoque.adicionar_lote(
            medicamento=medicamento,
            lote=dados["lote"],
            validade=dados["validade"],
            quantidade=dados["quantidade"]
        )

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

        try:
            quantidade = self.__tela_estoque.pega_quantidade_para_baixa()
            if quantidade < 0: 
                self.__tela_estoque.mostra_mensagem("Quantidade para baixa deve ser um número positivo.")
                return
            self.__estoque.abaixar_estoque(medicamento, quantidade)
            self.__tela_estoque.mostra_mensagem("Estoque baixado com sucesso.")
        except EstoqueInsuficiente:
            self.__tela_estoque.mostra_mensagem("Estoque insuficiente para a quantidade solicitada.")
        except ValueError:
            self.__tela_estoque.mostra_mensagem("Quantidade inválida.")

    def estoque_baixo(self):
        lotes_baixos = self.__estoque.estoque_baixo(limite=5) 

        if not lotes_baixos:
            self.__tela_estoque.mostra_mensagem("Nenhum medicamento com estoque baixo (quantidade abaixo de 5).")
            return

        self.__tela_estoque.mostra_mensagem("------ Medicamentos com Estoque Baixo ------")
        for lote in lotes_baixos:
            self.__tela_estoque.mostra_lote(lote)

    def consultar_total_medicamento(self, medicamento: Medicamento) -> int:
        return self.__estoque.consultar_estoque(medicamento)
    
    def realizar_baixa_medicamento(self, medicamento: Medicamento, quantidade: int): 
        if not isinstance(medicamento, Medicamento):
            raise TypeError("O argumento 'medicamento' deve ser uma instância de Medicamento.")
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("A quantidade deve ser um número inteiro positivo.")
            
        self.__estoque.abaixar_estoque(medicamento, quantidade)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.listar_estoque,
            2: self.aumentar_estoque,
            3: self.abaixar_estoque,
            4: self.estoque_baixo,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_estoque.tela_opcoes()
            if opcao == -1: 
                continue
            
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
            elif opcao == 0:
                break
            else:
                self.__tela_estoque.mostra_mensagem("Opção inválida. Por favor, escolha uma das opções acima.")