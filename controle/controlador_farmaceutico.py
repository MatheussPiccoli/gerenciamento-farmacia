from limite.tela_farmaceutico import TelaFarmaceutico
from Models.farmaceutico import Farmaceutico
from controle.exceptions import FarmaceuticoNaoExistente, FarmaceuticoNaoEncontrado
from DAOs.farmaceutico_dao import farmaceuticoDAO


class ControladorFarmaceutico():
    def __init__(self, controlador_sistema):
        self.__farmaceutico_DAO = farmaceuticoDAO()
        self.__tela_farmaceutico = TelaFarmaceutico()
        self.__controlador_sistema = controlador_sistema

    
    def pega_farmaceutico_por_cpf(self, cpf: str):
        for farmaceutico in self.__farmaceutico_DAO.get_all():
            print(farmaceutico.cpf)
            if farmaceutico.cpf == cpf:
                return farmaceutico
        raise FarmaceuticoNaoEncontrado(f"farmaceutico com CPF '{cpf}' não encontrado.") 

    def incluir_farmaceutico(self):
        dados_farmaceutico = self.__tela_farmaceutico.pega_dados_farmaceutico()
        if dados_farmaceutico is None:
            self.__tela_farmaceutico.mostra_mensagem("Cadastro de farmaceutico cancelado.")
            return
        
        try:
            self.pega_farmaceutico_por_cpf(dados_farmaceutico["cpf"])
            self.__tela_farmaceutico.mostra_mensagem("Erro: Já existe um farmaceutico com este CPF.")
            return
        except FarmaceuticoNaoEncontrado:
            pass

        farmaceutico_obj = Farmaceutico(dados_farmaceutico["nome"], dados_farmaceutico["cpf"], dados_farmaceutico["salario"])
        self.__farmaceutico_DAO.add(farmaceutico_obj)
        self.__tela_farmaceutico.mostra_mensagem("farmaceutico cadastrado com sucesso!")
    
    def alterar_farmaceutico(self):
        self.lista_farmaceutico()
        cpf_farmaceutico = self.__tela_farmaceutico.seleciona_farmaceutico()
        if not cpf_farmaceutico: 
            self.__tela_farmaceutico.mostra_mensagem("Seleção de farmaceutico para alteração cancelada.")
            return

        try:
            farmaceutico = self.pega_farmaceutico_por_cpf(cpf_farmaceutico)
        except FarmaceuticoNaoEncontrado:
            self.__tela_farmaceutico.mostra_mensagem("farmaceutico não encontrado para alteração.")
            return

        novos_dados_farmaceutico = self.__tela_farmaceutico.pega_dados_farmaceutico()
        if novos_dados_farmaceutico is None:
            self.__tela_farmaceutico.mostra_mensagem("Alteração de farmaceutico cancelada.")
            return

        if novos_dados_farmaceutico["cpf"] != farmaceutico.cpf:
            try:
                self.pega_farmaceutico_por_cpf(novos_dados_farmaceutico["cpf"])
                self.__tela_farmaceutico.mostra_mensagem("Erro: O novo CPF já pertence a outro farmaceutico.")
                return
            except FarmaceuticoNaoEncontrado:
                pass
        if farmaceutico is not None:
            farmaceutico.nome = novos_dados_farmaceutico["nome"]
            farmaceutico.cpf = novos_dados_farmaceutico["cpf"]
            farmaceutico.salario = novos_dados_farmaceutico["salario"]
            
            self.__tela_farmaceutico.mostra_mensagem("farmaceutico alterado com sucesso!")
            self.__farmaceutico_DAO.update(farmaceutico)
            self.lista_farmaceutico()
        else:
            self.__tela_farmaceutico.mostra_mensagem("farmaceutico não encontrado para alteração.")
            return

    def lista_farmaceutico(self):
        if not self.__farmaceutico_DAO.get_all():
            self.__tela_farmaceutico.mostra_mensagem("Nenhum farmaceutico cadastrado.")
            return

        dados_farmaceutico = []
        for farmaceutico in self.__farmaceutico_DAO.get_all():
            dados_farmaceutico.append({"nome": farmaceutico.nome, "cpf": farmaceutico.cpf,
                                                 "salario": farmaceutico.salario, "id": farmaceutico.id})
        self.__tela_farmaceutico.mostra_farmaceuticos(dados_farmaceutico)

    def excluir_farmaceutico(self):
        self.lista_farmaceutico()
        cpf_farmaceutico = self.__tela_farmaceutico.seleciona_farmaceutico()
        if not cpf_farmaceutico:
            self.__tela_farmaceutico.mostra_mensagem("Seleção de farmaceutico para exclusão cancelada.")
            return

        try:
            farmaceutico = self.pega_farmaceutico_por_cpf(cpf_farmaceutico)
        except FarmaceuticoNaoEncontrado:
            self.__tela_farmaceutico.mostra_mensagem("farmaceutico não encontrado para exclusão.")
            return

        if farmaceutico is not None:
            self.__farmaceutico_DAO.remove(farmaceutico.cpf)
            self.__tela_farmaceutico.mostra_mensagem("farmaceutico excluído com sucesso!")
            self.lista_farmaceutico()
        else:
            self.__tela_farmaceutico.mostra_mensagem("farmaceutico não encontrado para exclusão.")
            return
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_farmaceutico,
            2: self.alterar_farmaceutico,
            3: self.lista_farmaceutico,
            4: self.excluir_farmaceutico,
            0: self.retornar
        }

        continua = True
        while continua:
            opcao = self.__tela_farmaceutico.tela_opcoes()
            if opcao == -1:
                continue

            funcao = lista_opcoes.get(opcao)
            if funcao:
                try:
                    funcao()
                except FarmaceuticoNaoExistente as erro:
                    self.__tela_farmaceutico.mostra_mensagem(erro.args[0])
                except FarmaceuticoNaoEncontrado as erro:
                    self.__tela_farmaceutico.mostra_mensagem(erro.args[0])
                except Exception as erro:
                    self.__tela_farmaceutico.mostra_mensagem(f"Ocorreu um erro: {erro}")
            elif opcao == 0:
                continua = False 
            else:
                self.__tela_farmaceutico.mostra_mensagem("Opção inválida. Escolha uma das opções acima.")
