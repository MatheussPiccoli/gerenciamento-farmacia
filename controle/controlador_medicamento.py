from limite.tela_medicamento import TelaMedicamento
from Models.medicamento import Medicamento
from controle.exceptions import MedicamentoNaoEncontrado


class ControladorMedicamento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__medicamentos = []
        self.__tela_medicamento = TelaMedicamento() 
        self.cria_medicamentos_iniciais()

    def cria_medicamentos_iniciais(self):
        Medicamento.contador_id = 0

        medicamento1 = Medicamento("Paracetamol", "Genérico", 5.50)
        medicamento2 = Medicamento("Ibuprofeno", "EMS", 12.00)
        medicamento3 = Medicamento("Amoxicilina", "Neo Química", 25.00)
        medicamento4 = Medicamento("Paracetamol", "EMS", 7.00)
        
        self.__medicamentos.append(medicamento1)
        self.__medicamentos.append(medicamento2)
        self.__medicamentos.append(medicamento3)
        self.__medicamentos.append(medicamento4)

    def pega_medicamento_por_nome(self, nome: str) -> Medicamento:
        medicamentos_encontrados = [
            m for m in self.__medicamentos if m.nome.lower() == nome.lower()
        ]

        if not medicamentos_encontrados:
            raise MedicamentoNaoEncontrado(f"Medicamento com nome '{nome}' não encontrado.")

        elif len(medicamentos_encontrados) == 1:
            return medicamentos_encontrados[0]

        else:
            self.__tela_medicamento.mostra_opcoes_medicamentos(medicamentos_encontrados)
            
            try:
                opcao = self.__tela_medicamento.pede_opcao_medicamento(len(medicamentos_encontrados))
            except ValueError:
                raise MedicamentoNaoEncontrado("Seleção de medicamento cancelada ou inválida.")

            if opcao is None or not (1 <= opcao <= len(medicamentos_encontrados)):
                raise MedicamentoNaoEncontrado("Opção de medicamento inválida. Seleção cancelada.")
            
            return medicamentos_encontrados[opcao - 1]

    def seleciona_medicamento(self):
        nome = self.__tela_medicamento.pede_nome_medicamento()
        if not nome:
            raise MedicamentoNaoEncontrado("Seleção de medicamento cancelada.")
            
        try:
            return self.pega_medicamento_por_nome(nome)
        except MedicamentoNaoEncontrado:
            raise

    def incluir_medicamento(self):
        dados_medicamento = self.__tela_medicamento.pega_dados_medicamento()
        if dados_medicamento is None:
            self.__tela_medicamento.mostra_msg("Operação cancelada.")
            return
        medicamento = Medicamento(dados_medicamento["nome"],
                                  dados_medicamento["fabricante"],
                                  dados_medicamento["preco"])
        self.__medicamentos.append(medicamento)
        self.__tela_medicamento.mostra_msg("Medicamento registrado com sucesso.")

    def alterar_ou_excluir_medicamento(self):
        try:
            medicamento = self.seleciona_medicamento()
            opcao = self.__tela_medicamento.mostra_opcoes_de_acao()

            if opcao == 1:
                novos_dados = self.__tela_medicamento.pega_dados_medicamento()
                if novos_dados is None:
                    self.__tela_medicamento.mostra_msg("Operação cancelada.")
                    return
                medicamento.nome = novos_dados["nome"]
                medicamento.fabricante = novos_dados["fabricante"]
                medicamento.preco = novos_dados["preco"]
                self.__tela_medicamento.mostra_msg("Medicamento alterado com sucesso.")


            elif opcao == 2:
                self.__medicamentos.remove(medicamento)
                self.__tela_medicamento.mostra_msg("Medicamento removido com sucesso.")

            elif opcao == 0:
                self.__tela_medicamento.mostra_msg("Operação cancelada.")

            else:
                self.__tela_medicamento.mostra_msg("Opção inválida.")

        except MedicamentoNaoEncontrado:
            self.__tela_medicamento.mostra_msg("Medicamento não encontrado.")

    def lista_medicamentos(self):
        if len(self.__medicamentos) == 0:
            self.__tela_medicamento.mostra_msg("Não há nenhum medicamento registrado no sistema")
            return
        self.__tela_medicamento.mostra_lista_medicamentos(self.__medicamentos)

    def get_medicamentos(self):
        return self.__medicamentos

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_medicamento,
            2: self.alterar_ou_excluir_medicamento,
            3: self.lista_medicamentos,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_medicamento.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
