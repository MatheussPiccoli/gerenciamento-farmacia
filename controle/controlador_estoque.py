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

    def cria_estoque_inicial(self):
        medicamentos = self.__controlador_sistema.controlador_medicamento.get_all_medicamentos()

        if len(medicamentos) > 0:
            estoque = self.__estoque_dao.get_estoque()
            paracetamol_generico = next((m for m in medicamentos if m.nome == "Paracetamol" and m.fabricante == "Genérico"), None)
            ibuprofeno_ems = next((m for m in medicamentos if m.nome == "Ibuprofeno" and m.fabricante == "EMS"), None)
            
            if paracetamol_generico:
                estoque.adicionar_lote(
                    medicamento=paracetamol_generico,
                    lote="P12345",
                    validade=date(2026, 12, 31), 
                    quantidade=500
                )
                estoque.adicionar_lote(
                    medicamento=paracetamol_generico,
                    lote="P67890",
                    validade=date(2025, 6, 30), 
                    quantidade=200
                )
            if ibuprofeno_ems:
                estoque.adicionar_lote(
                    medicamento=ibuprofeno_ems,
                    lote="I12345",
                    validade=date(2027, 1, 15),
                    quantidade=300
                )
            self.__estoque_dao.update(estoque)
            self.__tela_estoque.mostra_mensagem("Estoque inicial carregado.") 

    def listar_estoque(self):
        estoque = self.__estoque_dao.get_estoque()
        lotes = estoque.lotes
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

        estoque = self.__estoque_dao.get_estoque()
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

        try:
            quantidade = self.__tela_estoque.pega_quantidade_para_baixa()
            if quantidade < 0: 
                self.__tela_estoque.mostra_mensagem("Quantidade para baixa deve ser um número positivo.")
                return
            estoque = self.__estoque_dao.get_estoque()
            estoque.abaixar_estoque(medicamento, quantidade)
            self.__estoque_dao.update(estoque)
            self.__tela_estoque.mostra_mensagem("Estoque baixado com sucesso.")
        except EstoqueInsuficiente:
            self.__tela_estoque.mostra_mensagem("Estoque insuficiente para a quantidade solicitada.")
            
        except ValueError:
            self.__tela_estoque.mostra_mensagem("Quantidade inválida.")

    def estoque_baixo(self):
        estoque = self.__estoque_dao.get_estoque()
        lotes_baixos = estoque.estoque_baixo(limite=5) 

        if not lotes_baixos:
            self.__tela_estoque.mostra_mensagem("Nenhum medicamento com estoque baixo (quantidade abaixo de 5).")
            return

        self.__tela_estoque.mostra_mensagem("------ Medicamentos com Estoque Baixo ------")
        for lote in lotes_baixos:
            self.__tela_estoque.mostra_lote(lote)

    def consultar_total_medicamento(self, medicamento: Medicamento) -> int:
        estoque = self.__estoque_dao.get_estoque()
        return estoque.consultar_estoque(medicamento)
    
    def realizar_baixa_medicamento(self, medicamento: Medicamento, quantidade: int): 
        if not isinstance(medicamento, Medicamento):
            raise TypeError("O argumento 'medicamento' deve ser uma instância de Medicamento.")
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("A quantidade deve ser um número inteiro positivo.")
            
        estoque = self.__estoque_dao.get_estoque()
        estoque.abaixar_estoque(medicamento, quantidade)
        self.__estoque_dao.update(estoque)

    def lotes_vencidos(self):
        estoque = self.__estoque_dao.get_estoque()
        lotes_vencidos = estoque.lotes_vencidos()
        if not lotes_vencidos:
            self.__tela_estoque.mostra_mensagem("Nenhum lote vencido encontrado.")
            return

        self.__tela_estoque.mostra_mensagem("------ Lotes Vencidos ------")
        for lote in lotes_vencidos:
            self.__tela_estoque.mostra_lote(lote)

    def lotes_proximos_vencimento(self):
        estoque = self.__estoque_dao.get_estoque()
        lotes_proximos = estoque.lotes_proximos_vencimento(dias_limite=30)
        if not lotes_proximos:
            self.__tela_estoque.mostra_mensagem("Nenhum lote próximo ao vencimento encontrado.")
            return
        self.__tela_estoque.mostra_mensagem("------ Lotes Próximos ao Vencimento ------")
        for lote in lotes_proximos:
            self.__tela_estoque.mostra_lote(lote)

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
