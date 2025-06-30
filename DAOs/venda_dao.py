from DAOs.dao import DAO
from Models.venda import Venda

class VendaDAO(DAO):
    def __init__(self):
        super().__init__('vendas.pkl')

    def add(self, venda: Venda):
        if venda is not None and isinstance(venda, Venda) and isinstance(venda.id, int):
            super().add(venda.id, venda)

    def update(self, venda: Venda):
        if venda is not None and isinstance(venda, Venda) and isinstance(venda.id, int):
            super().update(venda.id, venda)

    def get(self, id: int) -> Venda | None:
        if isinstance(id, int):
            return super().get(id)
        return None

    def remove(self, id: int):
        if isinstance(id, int):
            super().remove(id) 