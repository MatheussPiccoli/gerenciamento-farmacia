from limite.tela_lote_medicamento import TelaLoteMedicamento
from Models.lote import LoteMedicamento
from controle.exceptions import MedicamentoNaoEncontrado
from datetime import date

class ControladorLoteMedicamento:
    def __init__(self, controlador_sistema):
        self.__lotes = []
        self.__tela_lote = TelaLoteMedicamento()
        self.__controlador_sistema = controlador_sistema

    def adicionar_lote(self):
        try:
            medicamento = self.__controlador_sistema.controlador_medicamento.seleciona_medicamento()
            dados = self.__tela_lote.pega_dados_lote()
            if not dados:
                self.__tela_lote.mostra_msg("Erro ao cadastrar lote.")
                return

            lote = LoteMedicamento(
                lote=dados["lote"],
                validade=dados["validade"],
                quantidade=dados["quantidade"],
                medicamento=medicamento
            )
            self.__lotes.append(lote)
            self.__tela_lote.mostra_msg("Lote cadastrado com sucesso.")

        except MedicamentoNaoEncontrado:
            self.__tela_lote.mostra_msg("Medicamento não encontrado.")

    def listar_lotes_por_medicamento(self):
        try:
            medicamento = self.__controlador_sistema.controlador_medicamento.seleciona_medicamento()
            lotes = [l for l in self.__lotes if l.medicamento.id == medicamento.id]

            if not lotes:
                self.__tela_lote.mostra_msg("Nenhum lote encontrado para esse medicamento.")
                return

            for lote in lotes:
                self.__tela_lote.mostra_lote({
                    "lote": lote.lote,
                    "validade": lote.validade.strftime("%d/%m/%Y"),
                    "quantidade": lote.quantidade
                })
        except MedicamentoNaoEncontrado:
            self.__tela_lote.mostra_msg("Medicamento não encontrado.")

    def verificar_lotes_vencidos(self):
        hoje = date.today()
        vencidos = [l for l in self.__lotes if l.validade < hoje]

        if not vencidos:
            self.__tela_lote.mostra_msg("Nenhum lote vencido.")
            return

        for lote in vencidos:
            self.__tela_lote.mostra_lote({
                "lote": lote.lote,
                "validade": lote.validade.strftime("%d/%m/%Y"),
                "quantidade": lote.quantidade
            })

    def verificar_validade_proxima(self):
        hoje = date.today()
        dias_limite = 30
        proximos = [l for l in self.__lotes if 0 <= (l.validade - hoje).days <= dias_limite]

        if not proximos:
            self.__tela_lote.mostra_msg("Nenhum lote com validade próxima.")
            return

        for lote in proximos:
            self.__tela_lote.mostra_lote({
                "lote": lote.lote,
                "validade": lote.validade.strftime("%d/%m/%Y"),
                "quantidade": lote.quantidade
            })

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = { 
            1: self.listar_lotes_por_medicamento,
            2: self.verificar_lotes_vencidos,
            3: self.verificar_validade_proxima,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_lote.tela_opcoes()
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
