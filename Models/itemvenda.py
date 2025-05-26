from Models.medicamento import Medicamento 

class ItemVenda:
    contador_id = 0 

    def __init__(self, medicamento: Medicamento, quantidade: int):
        if not isinstance(medicamento, Medicamento):
            raise TypeError("O argumento 'medicamento' deve ser uma instância de Medicamento.")
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("A 'quantidade' deve ser um número inteiro positivo.")

        self.__medicamento = medicamento
        self.__quantidade = quantidade
        self.__id = ItemVenda.contador_id 
        ItemVenda.contador_id += 1 
        self.calcular_subtotal() 

    @property
    def medicamento(self):
        return self.__medicamento

    @medicamento.setter
    def medicamento(self, medicamento):
        if not isinstance(medicamento, Medicamento):
            raise TypeError("O argumento 'medicamento' deve ser uma instância de Medicamento.")
        self.__medicamento = medicamento
        self.calcular_subtotal()

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("A 'quantidade' deve ser um número inteiro positivo.")
        self.__quantidade = quantidade
        self.calcular_subtotal()

    @property
    def subtotal(self):
        return self.__subtotal
    
    @property
    def id(self):
        return self.__id

    def calcular_subtotal(self):
        self.__subtotal = self.__quantidade * self.__medicamento.preco