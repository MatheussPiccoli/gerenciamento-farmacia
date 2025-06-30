import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = []
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
    
    def dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))
    
    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))
    
    def add(self, obj):
        self.__cache.append(obj)
        self.__dump()
    
    def update(self, obj):
        try:
            if(self.__cache.index(obj) != None):
                self.__cache[self.__cache.index(obj)] = obj
                self.__dump()
        except KeyError:
            pass
    
    def get(self, obj):
        try:
            return self.__cache[self.__cache.index(obj)]
        except ValueError:
            return None

    def get_all(self):
        return self.__cache.values()

    def remove(self, obj):
        try:
            self.__cache.remove(obj)
            self.__dump()
        except ValueError:
            pass
