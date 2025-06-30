import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = []
        self.__load()
    
    def __dump(self):
        with open(self.__datasource, 'wb') as file:
            pickle.dump(self.__cache, file)
    
    def __load(self):
        try:
            with open(self.__datasource, 'rb') as file:
                self.__cache = pickle.load(file)
        except (FileNotFoundError, EOFError):
            # Se o arquivo não existe ou está vazio/corrompido, inicializa cache vazio
            self.__cache = []
            self.__dump()
    
    def add(self, key, obj):
        # Remove objeto existente com a mesma chave, se houver
        self.remove(key)
        # Adiciona o novo objeto
        self.__cache.append(obj)
        self.__dump()
    
    def update(self, key, obj):
        # Encontra e atualiza o objeto pela chave
        for i, item in enumerate(self.__cache):
            if self._get_key(item) == key:
                self.__cache[i] = obj
                self.__dump()
                return
    
    def get(self, key):
        # Procura pelo objeto com a chave especificada
        for item in self.__cache:
            if self._get_key(item) == key:
                return item
        return None

    def get_all(self):
        return self.__cache

    def remove(self, key):
        # Remove objeto pela chave
        self.__cache = [item for item in self.__cache if self._get_key(item) != key]
        self.__dump()
    
    def _get_key(self, obj):
        # Método auxiliar para extrair a chave do objeto
        # Deve ser sobrescrito pelos DAOs específicos se necessário
        if hasattr(obj, 'cpf'):
            return obj.cpf
        elif hasattr(obj, 'nome'):
            return obj.nome
        elif hasattr(obj, 'id'):
            return obj.id
        return str(obj)
