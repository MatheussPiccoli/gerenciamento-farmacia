# Models/venda.py
from Models.cliente import Cliente
from Models.itemvenda import ItemVenda
from datetime import date

class Venda:
    contador_id = 0

    def __init__(self, cliente: Cliente, farmaceutico, data: date, itens_dados: list):
        if not isinstance(cliente, Cliente): 
            raise TypeError("O argumento 'cliente' deve ser uma instância de Cliente.")
        if not isinstance(data, date):
            raise TypeError("O argumento 'data' deve ser uma instância de date.")

        self.__cliente = cliente
        self.__farmaceutico = farmaceutico
        self.__data = data
        self.__itens = [ItemVenda(**dados) for dados in itens_dados]  # Composição
        self.__valor_total = 0.0
        self.__id = Venda.contador_id
        Venda.contador_id += 1

    @property
    def id(self):
        return self.__id

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if not isinstance(cliente, Cliente): 
            raise TypeError("O argumento 'cliente' deve ser uma instância de Cliente.")
        self.__cliente = cliente

    @property
    def farmaceutico(self):
        return self.__farmaceutico

    @farmaceutico.setter
    def farmaceutico(self, farmaceutico):
        from Models.farmaceutico import Farmaceutico 
        if not isinstance(farmaceutico, Farmaceutico):
            raise TypeError("O argumento 'farmaceutico' deve ser uma instância de Farmaceutico.")
        self.__farmaceutico = farmaceutico

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, date):
            raise TypeError("O argumento 'data' deve ser uma instância de date.")
        self.__data = data

    @property
    def itens(self):
        return self.__itens

    def _adicionar_item(self, item : ItemVenda):
        if not isinstance(item, ItemVenda):
            raise TypeError("O item a ser adicionado deve ser uma instância de ItemVenda.")
        self.__itens.append(item)
        self.valor_total()

    def remover_item(self, item : ItemVenda):
        if item in self.__itens:
            self.__itens.remove(item)
            self.valor_total()
        else:
            raise ValueError("Item não encontrado na venda.")

    def valor_total(self):
        self.__valor_total = sum(item.subtotal for item in self.__itens)
        return self.__valor_total