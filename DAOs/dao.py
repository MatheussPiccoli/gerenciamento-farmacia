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
            self.__cache = []
            self.__dump()
    
    def add(self, key, obj):
        self.remove(key)
        self.__cache.append(obj)
        self.__dump()
    
    def update(self, key, obj):
        for i, item in enumerate(self.__cache):
            if self._get_key(item) == key:
                self.__cache[i] = obj
                self.__dump()
                return
    
    def get(self, key):
        for item in self.__cache:
            if self._get_key(item) == key:
                return item
        return None

    def get_all(self):
        return self.__cache

    def remove(self, key):
        self.__cache = [item for item in self.__cache if self._get_key(item) != key]
        self.__dump()
    
    def _get_key(self, obj):
        if hasattr(obj, 'cpf'):
            return obj.cpf
        elif hasattr(obj, 'nome'):
            return obj.nome
        elif hasattr(obj, 'id'):
            return obj.id
        return str(obj)
