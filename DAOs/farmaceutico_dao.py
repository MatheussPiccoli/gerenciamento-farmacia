from DAOs.dao import DAO
from Models.farmaceutico import Farmaceutico


class farmaceuticoDAO(DAO):
    def __init__(self):
        super().__init__('farmaceuticos.pkl')
    
    def add(self, farmaceutico: Farmaceutico):
        if ((farmaceutico is not None) and isinstance(farmaceutico, Farmaceutico) \
            and isinstance(farmaceutico.cpf, str) and isinstance(farmaceutico.salario, float)):
            super().add(farmaceutico.cpf, farmaceutico)

    def update(self, farmaceutico: Farmaceutico):
        if ((farmaceutico is not None) and isinstance(farmaceutico, farmaceutico) \
            and isinstance(farmaceutico.cpf, str) and isinstance(farmaceutico.salario)):
            super().update(farmaceutico.cpf, farmaceutico)

    def get(self, cpf: str) -> Farmaceutico:
        if isinstance(cpf, str):
            return super().get(cpf)
        return None

    def remove(self, cpf: str):
        if isinstance(cpf, str):
            super().remove(cpf)

