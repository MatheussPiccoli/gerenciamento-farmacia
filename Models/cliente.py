from Models.pessoa import Pessoa

class Cliente(Pessoa):

    contador_id = 0

    def __init__(self, nome: str, cpf: str, telefone: str):
        super().__init__(nome, cpf, Cliente.contador_id)
        self.__telefone = telefone
        self.__id = Cliente.contador_id
        Cliente.contador_id += 1

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id