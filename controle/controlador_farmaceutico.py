from limite.tela_farmaceutico import TelaFarmaceutico
from Models.farmaceutico import Farmaceutico
from controle.exceptions import FarmaceuticoNaoExistente, FarmaceuticoNaoEncontrado


class ControladorFarmaceutico():
    def __init__(self, controlador_sistema):
        self.__farmaceuticos = []
        self.__tela_farmaceutico = TelaFarmaceutico()
        self.__controlador_sistema = controlador_sistema
        self.cria_farmaceuticos_iniciais()

    def cria_farmaceuticos_iniciais(self):
        Farmaceutico.contador_id = 0
        farmaceutico1 = Farmaceutico("Dr. João Saúde", "12345678901", 3500.00)
        farmaceutico2 = Farmaceutico("Dra. Maria Cura", "09876543210", 4000.00)
        
        self.__farmaceuticos.append(farmaceutico1)
        self.__farmaceuticos.append(farmaceutico2)
    
    def pega_farmaceutico_por_cpf(self, cpf: str):
        for farmaceutico in self.__farmaceuticos:
            if(farmaceutico.cpf == cpf):
                return farmaceutico
        raise FarmaceuticoNaoEncontrado(f"Farmacêutico com CPF '{cpf}' não encontrado.") 

    def incluir_farmaceutico(self):
        dados_farmaceutico = self.__tela_farmaceutico.pega_dados_farmaceutico()
        if dados_farmaceutico is None:
            self.__tela_farmaceutico.mostra_mensagem("Cadastro de farmacêutico cancelado.")
            return

        try:
            self.pega_farmaceutico_por_cpf(dados_farmaceutico["cpf"])
            self.__tela_farmaceutico.mostra_mensagem("Erro: Já existe um farmacêutico com este CPF.")
            return
        except FarmaceuticoNaoEncontrado:
            pass

        farmaceutico = Farmaceutico(
            dados_farmaceutico["nome"],
            dados_farmaceutico["cpf"],
            dados_farmaceutico["salario"]
        )
        self.__farmaceuticos.append(farmaceutico)
        self.__tela_farmaceutico.mostra_mensagem("Farmacêutico cadastrado com sucesso!")
    
    def alterar_farmaceutico(self):
        self.lista_farmaceuticos()
        cpf_farmaceutico = self.__tela_farmaceutico.seleciona_farmaceutico()
        if not cpf_farmaceutico:
            self.__tela_farmaceutico.mostra_mensagem("Seleção de farmacêutico para alteração cancelada.")
            return

        try:
            farmaceutico = self.pega_farmaceutico_por_cpf(cpf_farmaceutico)
        except FarmaceuticoNaoEncontrado:
            self.__tela_farmaceutico.mostra_mensagem("Farmacêutico não encontrado para alteração.")
            return

        novos_dados_farmaceutico = self.__tela_farmaceutico.pega_dados_farmaceutico()
        if novos_dados_farmaceutico is None:
            self.__tela_farmaceutico.mostra_mensagem("Alteração de farmacêutico cancelada.")
            return

        if novos_dados_farmaceutico["cpf"] != farmaceutico.cpf:
            try:
                self.pega_farmaceutico_por_cpf(novos_dados_farmaceutico["cpf"])
                self.__tela_farmaceutico.mostra_mensagem("Erro: O novo CPF já pertence a outro farmacêutico.")
                return
            except FarmaceuticoNaoEncontrado:
                pass

        farmaceutico.nome = novos_dados_farmaceutico["nome"]
        farmaceutico.cpf = novos_dados_farmaceutico["cpf"]
        farmaceutico.salario = novos_dados_farmaceutico["salario"]
        self.__tela_farmaceutico.mostra_mensagem("Farmacêutico alterado com sucesso!")
        self.lista_farmaceuticos()

    def lista_farmaceuticos(self):
        if not self.__farmaceuticos:
            self.__tela_farmaceutico.mostra_mensagem("Nenhum farmacêutico cadastrado.")
            return
        
        for farmaceutico in self.__farmaceuticos:
            self.__tela_farmaceutico.mostra_farmaceutico({
                "nome": farmaceutico.nome,
                "cpf": farmaceutico.cpf,
                "salario": farmaceutico.salario
            })

    def excluir_farmaceutico(self):
        self.lista_farmaceuticos()
        cpf_farmaceutico = self.__tela_farmaceutico.seleciona_farmaceutico()
        if not cpf_farmaceutico: # Se a tela retornou um CPF inválido
            self.__tela_farmaceutico.mostra_mensagem("Seleção de farmacêutico para exclusão cancelada.")
            return

        try:
            farmaceutico = self.pega_farmaceutico_por_cpf(cpf_farmaceutico)
        except FarmaceuticoNaoEncontrado:
            self.__tela_farmaceutico.mostra_mensagem("Farmacêutico não encontrado para exclusão.")
            return

        self.__farmaceuticos.remove(farmaceutico)
        self.__tela_farmaceutico.mostra_mensagem("Farmacêutico excluído com sucesso!")
        self.lista_farmaceuticos()
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_farmaceutico,
            2: self.alterar_farmaceutico,
            3: self.lista_farmaceuticos,
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
                continua = False # Quebra o loop do farmacêutico
            else:
                self.__tela_farmaceutico.mostra_mensagem("Opção inválida. Escolha uma das opções acima.")