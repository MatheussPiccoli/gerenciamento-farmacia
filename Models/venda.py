from cliente import Cliente
from farmaceutico import Farmaceutico
from datetime import date
from itemvenda import ItemVenda


class Venda:
    def __init__(self, cliente: Cliente, farmaceutico: Farmaceutico, data: date, itens, valor_total: float):
        if isinstance(cliente, Cliente): 
            self.__cliente = cliente
        if isinstance(farmaceutico, Farmaceutico): 
            self.__farmaceutico = farmaceutico
        self.__data = data
        self.__itens = list(itens)
        self.__valor_total = valor_total

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def farmaceutico(self):
        return self.__farmaceutico

    @farmaceutico.setter
    def farmaceutico(self, farmaceutico):
        self.__farmaceutico = farmaceutico

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def itens(self):
        return self.__itens

    @itens.setter
    def itens(self, itens):
        self.__itens = itens

    def adicionar_item(self, item: ItemVenda):
        self.__itens.append(item)

    def valor_total(self):
        self.__valor_total = sum(item.subtotal for item in self.__itens)
        return self.__valor_total
