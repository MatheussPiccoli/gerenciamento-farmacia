class Medicamento():
    contador_id = 0

    def __init__(self, nome : str, fabricante : str, preco : float):
        self.__nome = nome
        self.__fabricante = fabricante
        self.__preco = preco
        self.__id = Medicamento.contador_id
        Medicamento.contador_id += 1

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def fabricante(self):
        return self.__fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        if isinstance(fabricante, str):
            self.__fabricante = fabricante

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        if isinstance(preco, float):
            self.__preco = preco