import pickle
from Models.estoque import Estoque


class EstoqueDAO:
    def __init__(self):
        self.__datasource = 'estoque.pkl'
        self.__estoque = None
        self.__load()

    def __load(self):
        try:
            with open(self.__datasource, 'rb') as file:
                loaded_data = pickle.load(file)
                if isinstance(loaded_data, Estoque):
                    self.__estoque = loaded_data
                else:
                    self.__estoque = Estoque()
                    self.__dump()
        except (FileNotFoundError, EOFError):
            self.__estoque = Estoque()
            self.__dump()

    def __dump(self):
        with open(self.__datasource, 'wb') as file:
            pickle.dump(self.__estoque, file)

    def get_estoque(self):
        return self.__estoque

    def update(self, estoque: Estoque):
        if estoque is not None and isinstance(estoque, Estoque):
            self.__estoque = estoque
            self.__dump()
