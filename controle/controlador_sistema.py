from limite.tela_sistema import TelaSistema
from controle.controlador_farmaceutico import ControladorFarmaceutico
from controle.controlador_cliente import Controladorclientes
from controle.controlador_venda import ControladorVenda
from controle.controlador_estoque import ControladorEstoque
from controle.controlador_medicamento import ControladorMedicamento
from controle.controlador_relatorios import RelatorioController


class ControladorSistema:

    def __init__(self):
        self.__controlador_clientes = Controladorclientes(self)
        self.__controlador_farmaceutico = ControladorFarmaceutico(self)
        self.__controlador_estoque = ControladorEstoque(self)
        self.__controlador_medicamento = ControladorMedicamento(self)
        self.__tela_sistema = TelaSistema()
        self.__controlador_relatorios = RelatorioController(self)
        self.__controlador_venda = ControladorVenda(self)


    @property
    def controlador_cliente(self):
        return self.__controlador_clientes
    
    @property
    def controlador_farmaceutico(self):
        return self.__controlador_farmaceutico
    
    @property
    def controlador_venda(self):
        return self.__controlador_venda
    
    @property
    def controlador_estoque(self):
        return self.__controlador_estoque
    
    @property
    def controlador_medicamento(self):
        return self.__controlador_medicamento
    
    @property
    def controlador_relatorios(self):
        return self.__controlador_relatorios
    

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_cliente(self):
        self.__controlador_clientes.abre_tela()
    
    def cadastra_farmaceutico(self):
        self.__controlador_farmaceutico.abre_tela()

    def cadastra_medicamento(self):
        self.__controlador_medicamento.abre_tela()

    def inicia_venda(self):
        self.__controlador_venda.abre_tela()

    def abre_estoque(self):
        self.__controlador_estoque.abre_tela()

    def relatorios(self):
        self.__controlador_relatorios.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_cliente, 
                        2: self.cadastra_farmaceutico,
                        3:self.inicia_venda, 
                        4: self.abre_estoque, 
                        5: self.cadastra_medicamento,
                        6: self.relatorios, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()