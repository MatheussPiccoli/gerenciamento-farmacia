from pessoa import Pessoa
from venda import Venda


class Farmaceutico(Pessoa):
    def __init__(self, nome: str, cpf: str, id: int, salario: int):
        super().__init__(nome, cpf, id)
        self.__salario = salario
        self.__vendas = []

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    def registrar_venda(self, venda: Venda):
        if venda not in self.__vendas and isinstance(venda, Venda):
            self.__vendas.append(venda)
