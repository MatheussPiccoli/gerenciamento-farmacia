from medicamento import Medicamento


class ItemVenda:
    def __init__(self, medicamento: Medicamento, quantidade: int):
        if isinstance(medicamento, Medicamento):
            self.__medicamento = medicamento
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
        self.__subtotal = self.calcular_subtotal

    @property
    def medicamento(self):
        return self.__medicamento
    
    @medicamento.setter
    def medicamento(self, medicamento):
        if isinstance(medicamento, Medicamento):
            self.__medicamento = medicamento
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade

    @property
    def subtotal(self):
        return self.__subtotal
    
    def calcular_subtotal(self):
        self.__subtotal = self.__quantidade * self.__medicamento.preco
