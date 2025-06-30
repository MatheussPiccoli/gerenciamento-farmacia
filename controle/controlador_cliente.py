from limite.tela_cliente import TelaCliente
from Models.cliente import Cliente
from controle.exceptions import ClienteNaoEncontrado
from DAOs.cliente_dao import ClienteDAO


class Controladorclientes():

    def __init__(self, controlador_sistema):
        self.__clientes_DAO = ClienteDAO()
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema

    def pega_cliente_por_cpf(self, cpf: str):
        for cliente in self.__clientes_DAO.get_all():
            print(cliente.cpf)
            if cliente.cpf == cpf:
                return cliente
        raise ClienteNaoEncontrado(f"Cliente com CPF '{cpf}' não encontrado.")

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        if dados_cliente is None:
            self.__tela_cliente.mostra_mensagem("Cadastro de cliente cancelado.")
            return
        
        try:
            self.pega_cliente_por_cpf(dados_cliente["cpf"])
            self.__tela_cliente.mostra_mensagem("Erro: Já existe um cliente com este CPF.")
            return
        except ClienteNaoEncontrado:
            pass

        cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], 
                            dados_cliente["telefone"])
        self.__clientes_DAO.add(cliente)
        self.__tela_cliente.mostra_mensagem("Cliente cadastrado com sucesso!")

    def alterar_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        if not cpf_cliente: 
            self.__tela_cliente.mostra_mensagem("Seleção de cliente para alteração cancelada.")
            return

        try:
            cliente = self.pega_cliente_por_cpf(cpf_cliente)
        except ClienteNaoEncontrado:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado para alteração.")
            return

        novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
        if novos_dados_cliente is None:
            self.__tela_cliente.mostra_mensagem("Alteração de cliente cancelada.")
            return

        if novos_dados_cliente["cpf"] != cliente.cpf:
            try:
                self.pega_cliente_por_cpf(novos_dados_cliente["cpf"])
                self.__tela_cliente.mostra_mensagem("Erro: O novo CPF já pertence a outro cliente.")
                return
            except ClienteNaoEncontrado:
                pass
        if cliente is not None:
            cliente.nome = novos_dados_cliente["nome"]
            cliente.cpf = novos_dados_cliente["cpf"]
            cliente.telefone = novos_dados_cliente["telefone"]
            
            self.__tela_cliente.mostra_mensagem("Cliente alterado com sucesso!")
            self.__clientes_DAO.update(cliente)
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado para alteração.")
            return

    def lista_clientes(self):
        if not self.__clientes_DAO.get_all():
            self.__tela_cliente.mostra_mensagem("Nenhum cliente cadastrado.")
            return

        dados_clientes = []
        for cliente in self.__clientes_DAO.get_all():
            dados_clientes.append({"nome": cliente.nome, "cpf": cliente.cpf,
                                                 "telefone": cliente.telefone, "id": cliente.id})
        self.__tela_cliente.mostra_clientes(dados_clientes)
            

    def excluir_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        if not cpf_cliente:
            self.__tela_cliente.mostra_mensagem("Seleção de cliente para exclusão cancelada.")
            return

        try:
            cliente = self.pega_cliente_por_cpf(cpf_cliente)
        except ClienteNaoEncontrado:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado para exclusão.")
            return

        if cliente is not None:
            self.__clientes_DAO.remove(cliente.cpf)
            self.__tela_cliente.mostra_mensagem("Cliente excluído com sucesso!")
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem("Cliente não encontrado para exclusão.")
            return

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 
                        2: self.alterar_cliente, 
                        3: self.lista_clientes, 
                        4: self.excluir_cliente, 
                        0: self.retornar}

        continua = True
        while continua:
            opcao = self.__tela_cliente.tela_opcoes()
            if opcao == -1:
                continue
            
            funcao = lista_opcoes.get(opcao)
            if funcao:
                try:
                    funcao()
                except ClienteNaoEncontrado as e:
                    self.__tela_cliente.mostra_mensagem(e.args[0])
                except Exception as e:
                    self.__tela_cliente.mostra_mensagem(f"Ocorreu um erro: {e}")
            elif opcao == 0:
                continua = False
            else:
                self.__tela_cliente.mostra_mensagem("Opção inválida. Escolha uma das opções acima.")
