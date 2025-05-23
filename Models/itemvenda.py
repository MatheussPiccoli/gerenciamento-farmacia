from Models.medicamento import Medicamento


class ItemVenda:

    contador_id = 0

    def __init__(self, medicamento: Medicamento, quantidade: int, id: int):
        self.__medicamento = medicamento
        self.__quantidade = quantidade
        self.__subtotal = self.__quantidade * self.__medicamento.preco
        self.__id = ItemVenda.contador_id
        ItemVenda.contador_id += 1

    @property
    def medicamento(self):
        return self.__medicamento

    @medicamento.setter
    def medicamento(self, medicamento):
        self.__medicamento = medicamento
        self.calcular_subtotal()

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
        self.calcular_subtotal()

    @property
    def subtotal(self):
        return self.__subtotal
    
    def calcular_subtotal(self):
        self.__subtotal = self.__quantidade * self.__medicamento.preco
