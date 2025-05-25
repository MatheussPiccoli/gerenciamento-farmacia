from limite.tela_relatorios import TelaRelatorios

class RelatorioController:
    def __init__(self, controlador_sistema):
        self.__tela_relatorio = TelaRelatorios()
        self.__controlador_sistema = controlador_sistema

    def get_vendas(self):
        return self.__vendas

    def vendas_por_periodo(self):

        self.__tela_relatorio.mostra_msg(">> Relatório de Vendas por Período")
        self.__tela_relatorio.mostra_msg("Selecione o período desejado:")
        data_inicio, data_fim = self.__tela_relatorio.pega_periodo()
        vendas = self.__controlador_sistema.controlador_venda.get_vendas()
        vendas_filtradas = [venda for venda in vendas if data_inicio <= venda.data <= data_fim]

        if not vendas_filtradas:
            self.__tela_relatorio.mostra_msg("Nenhuma venda encontrada nesse período.")
            return
        
        for venda in vendas_filtradas:
            self.__tela_relatorio.mostra_venda({
                "cliente": venda.cliente.nome,
                "farmaceutico": venda.farmaceutico.nome,
                "data": venda.data,
                "itens": venda.itens
            })

    def medicamentos_mais_vendidos(self):

        self.__tela_relatorio.mostra_msg(">> Relatório de Medicamentos mais Vendidos")
        self.__tela_relatorio.mostra_msg("Selecione o período desejado:")
        data_inicio, data_fim = self.__tela_relatorio.pega_periodo()
        medicamentos = self.__controlador_sistema.controlador_medicamento.get_medicamentos()
        medicamentos_filtrados = [medicamento for medicamento in medicamentos 
                                  if data_inicio <= medicamento.data_venda <= data_fim]
        
        for i in range(len(medicamentos_filtrados)):
            self.__tela_relatorio.mostra_msg(f"{i + 1}: {medicamentos_filtrados[i].nome}, {medicamentos_filtrados[i].quantidade_vendida} unidades vendidas")

    def clientes_que_mais_compraram(self):
        self.__tela_relatorio.mostra_msg(">> Relatório de Clientes que mais Compraram (em desenvolvimento)")

    def melhores_vendedores(self):
        self.__tela_relatorio.mostra_msg(">> Relatório de Melhores Vendedores (em desenvolvimento)")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.vendas_por_periodo,
            2: self.medicamentos_mais_vendidos,
            3: self.clientes_que_mais_compraram,
            4: self.melhores_vendedores,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_relatorio.tela_opcoes()
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
