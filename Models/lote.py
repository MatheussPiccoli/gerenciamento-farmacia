from medicamento import Medicamento
from datetime import date

class LoteMedicamento():

    contador_id = 0

    def __init__(self, medicamento : Medicamento, lote : str, validade: date, quantidade : int):

        self.__id = LoteMedicamento.contador_id
        LoteMedicamento.contador_id += 1

        if isinstance(medicamento, Medicamento):
            self.__medicamento = medicamento

        if isinstance(lote, str):
            self.__lote = lote

        self.__validade = validade

        if isinstance(quantidade, int):
            self.__quantidade = quantidade

    @property
    def medicamento(self):
        return self.__medicamento
    
    @medicamento.setter
    def medicamento(self, medicamento):
        if isinstance(medicamento, Medicamento):
            self.__medicamento = medicamento

    @property
    def lote(self):
        return self.__lote
    
    @lote.setter
    def lote(self, lote):
        if isinstance(lote, str):
            self.__lote = lote

    @property
    def validade(self):
        return self.__validade
    
    @validade.setter
    def validade(self, validade):
        if isinstance(validade, date):
            self.__validade = validade

    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade