from DAOs.dao import DAO
from Models.cliente import Cliente


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')
    
    def add(self, cliente: Cliente):
        if ((cliente is not None) and isinstance(cliente, Cliente) \
            and isinstance(cliente.cpf, str) and isinstance(cliente.telefone, str)):
            super().add(cliente.cpf, cliente)

    def update(self, cliente: Cliente):
        if ((cliente is not None) and isinstance(cliente, Cliente) \
            and isinstance(cliente.cpf, str) and isinstance(cliente.telefone, str)):
            super().update(cliente.cpf, cliente)

    def get(self, cpf: str) -> Cliente:
        if isinstance(cpf, str):
            return super().get(cpf)
        return None

    def remove(self, cpf: str):
        if isinstance(cpf, str):
            super().remove(cpf)

