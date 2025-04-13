from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf)
        self.__telefone = telefone

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone