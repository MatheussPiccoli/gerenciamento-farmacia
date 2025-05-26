
from Models.lote import LoteMedicamento
from Models.medicamento import Medicamento
from controle.exceptions import EstoqueInsuficiente
from datetime import date, timedelta

class Estoque:
    def __init__(self):
        self.__lotes = [] 

    def adicionar_lote(self, medicamento: Medicamento, lote: str, validade: date, quantidade: int):
        
        for lote_existente in self.__lotes:
            mesmo_medicamento = lote_existente.medicamento.id == medicamento.id
            mesmo_lote_identificador = lote_existente.lote == lote
            mesma_validade = lote_existente.validade == validade
            if mesmo_medicamento and mesmo_lote_identificador and mesma_validade:
                lote_existente.quantidade += quantidade
                return

        novo_lote = LoteMedicamento(medicamento, lote, validade, quantidade)
        self.__lotes.append(novo_lote)

    def abaixar_estoque(self, medicamento: Medicamento, quantidade: int):
        lotes_validos = sorted(
            [l for l in self.__lotes if l.medicamento.id == medicamento.id and l.quantidade > 0],
            key=lambda l: (l.validade, l.lote) 
        )

        restante = quantidade
        for lote in lotes_validos:
            if lote.quantidade >= restante:
                lote.quantidade -= restante
                if lote.quantidade == 0:
                    self.__lotes.remove(lote)
                return
            else:
                restante -= lote.quantidade
                lote.quantidade = 0
                self.__lotes.remove(lote)

        if restante > 0:
            raise EstoqueInsuficiente()

    def consultar_estoque(self, medicamento: Medicamento):
        total = sum(
            lote.quantidade for lote in self.__lotes if lote.medicamento.id == medicamento.id
        )
        return total if total > 0 else 0

    def estoque_baixo(self, limite=5):
        return [lote for lote in self.__lotes if lote.quantidade < limite]

    def lotes_vencidos(self):
        hoje = date.today()
        vencidos = [
            lote for lote in self.__lotes
            if lote.validade < hoje
        ]
        return vencidos

    def lotes_proximos_vencimento(self, dias_limite: int = 30):
        hoje = date.today()
        data_limite = hoje + timedelta(days=dias_limite)
        proximos = [
            lote for lote in self.__lotes
            if hoje <= lote.validade <= data_limite
        ]
        return proximos
    
    @property
    def lotes(self):
        return self.__lotes