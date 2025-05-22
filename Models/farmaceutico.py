from Models.pessoa import Pessoa
from Models.venda import Venda


class Farmaceutico(Pessoa):

    contador_id = 0

    def __init__(self, nome: str, cpf: str, id: int, salario: int):
        super().__init__(nome, cpf, id)
        self.__salario = salario
        self.__vendas = []
        self.__id = Farmaceutico.contador_id
        Farmaceutico.contador_id += 1

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def registrar_venda(self, venda: Venda):
        if venda not in self.__vendas and isinstance(venda, Venda):
            self.__vendas.append(venda)

