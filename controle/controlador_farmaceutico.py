from limite.tela_farmaceutico import TelaFarmaceutico
from Models.farmaceutico import Farmaceutico
from controle.exceptions import FarmaceuticoNaoExistente


class ControladorFarmaceutico():
    def __init__(self, controlador_sistema):
        self.__farmaceuticos = []
        self.__tela_farmaceutico = TelaFarmaceutico()
        self.__controlador_sistema = controlador_sistema
    
    def pega_farmaceutico_por_cpf(self, cpf: int):
        for farmaceutico in self.__farmaceuticos:
            if(farmaceutico.cpf == cpf):
                return farmaceutico
        return None
    
    def incluir_farmaceutico(self):
        dados_farmaceutico = self.__tela_farmaceutico.pega_dados_farmaceutico()
        farmaceutico = Farmaceutico(dados_farmaceutico["Nome"], dados_farmaceutico["CPF"], dados_farmaceutico["ID"],
                                    dados_farmaceutico["Salario"])
        self.__farmaceuticos.append(farmaceutico)
    
    def alterar_farmaceutico(self):
        self.lista_farmaceuticos()
        cpf_farmaceutico = self.__tela_farmaceutico.seleciona_farmaceutico()
        farmaceutico = self.pega_farmaceutico_por_cpf(cpf_farmaceutico)

        if(farmaceutico is not None):
            novos_dados_farmaceutico = self.__tela_farmaceutico.pega_dados_farmaceutico()
            farmaceutico.nome = novos_dados_farmaceutico["nome"]
            farmaceutico.cpf = novos_dados_farmaceutico["cpf"]
            farmaceutico.id = novos_dados_farmaceutico["ID"]
            farmaceutico.salario = novos_dados_farmaceutico["Salario"]
            self.lista_farmaceuticos()
        else:
            raise FarmaceuticoNaoExistente()

    def lista_farmaceuticos(self):
        for farmaceutico in self.__farmaceuticos:
            self.__tela_farmaceutico.mostra_farmaceutico({"nome": farmaceutico.nome, "cpf": farmaceutico.cpf,
                                                         "ID": farmaceutico.id, "Salario": farmaceutico.salario})

    def excluir_farmaceutico(self):
        self.lista_farmaceuticos()
        cpf_farmaceutico = self.__tela_farmaceutico.seleciona_farmaceutico()
        farmaceutico = self.pega_farmaceutico_por_cpf(cpf_farmaceutico)

        if(farmaceutico is not None):
            self.__farmaceuticos.remove(farmaceutico)
            self.lista_farmaceuticos()
        else:
            raise FarmaceuticoNaoExistente()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_farmaceutico, 2: self.alterar_farmaceutico, 3: self.lista_farmaceuticos,
                         4: self.excluir_farmaceutico, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_farmaceutico.tela_opcoes()]()
        
