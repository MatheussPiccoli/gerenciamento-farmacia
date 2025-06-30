from DAOs.dao import DAO
from Models.medicamento import Medicamento


class MedicamentoDAO(DAO):
    def __init__(self):
        super().__init__('medicamentos.pkl')

    def add(self, medicamento):
        if (medicamento is not None and isinstance(medicamento, Medicamento) and
                isinstance(medicamento.id, int) and isinstance(medicamento.nome, str) and
                isinstance(medicamento.fabricante, str) and isinstance(medicamento.preco, float)):
            super().add(medicamento.nome, medicamento)

    def update(self, medicamento):
        if (medicamento is not None and isinstance(medicamento, Medicamento) and
                isinstance(medicamento.id, str) and isinstance(medicamento.nome, str)):
            super().update(medicamento.nome, medicamento)

    def get(self, nome: str) -> Medicamento:
        if isinstance(nome, str):
            return super().get(nome)
        return None

    def remove(self, nome: str):
        if isinstance(nome, str):
            super().remove(nome)
