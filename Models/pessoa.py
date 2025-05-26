from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, id: int):
        self.__nome = nome
        self.__cpf = cpf
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
