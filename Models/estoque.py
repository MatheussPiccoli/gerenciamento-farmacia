from Models.lote import LoteMedicamento
from Models.medicamento import Medicamento

class Estoque():
    def __init__(self):
        self.__lotes = []

    def add_lote(self, lote : LoteMedicamento):
        if isinstance(lote, LoteMedicamento):
            self.__lotes.append(lote)

    def baixar_estoque(self, medicamento : Medicamento, quantidade : int):
            lotes_filtrados = []
            for lote in self.__lotes:
                mesmo_medicamento = lote.medicamento.nome == medicamento.nome
                tem_estoque = lote.quantidade > 0

                if mesmo_medicamento and tem_estoque:
                    lotes_filtrados.append(lote)

            lotes_validos = sorted(lotes_filtrados, key=lambda lote: lote.validade)
            restante = quantidade
            for lote in lotes_validos:
                if lote.quantidade >= restante:
                    lote.quantidade -= restante
                    return
                else:
                    restante -= lote.quantidade
                    lote.quantidade = 0
            if restante > 0:
                raise ValueError(f"Não há estoque suficiente para {medicamento.nome}.")

    def consultar_estoque(self, medicamento : Medicamento):
        for lote in self.__lotes:
            if lote.medicamento == medicamento:
                return lote.quantidade
        return
        

