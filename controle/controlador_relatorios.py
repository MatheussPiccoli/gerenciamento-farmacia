from limite.tela_relatorios import TelaRelatorios
from datetime import datetime, date

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
        vendas = self.__controlador_sistema.controlador_venda.get_vendas_por_periodo(data_inicio, data_fim)
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

        vendas_do_periodo = self.__controlador_sistema.controlador_venda.get_vendas_por_periodo(data_inicio, data_fim)
        
        medicamentos_vendidos_agregado = {}
        
        for venda in vendas_do_periodo:
            for item_venda in venda.itens:
                chave_medicamento = (item_venda.medicamento.nome, item_venda.medicamento.fabricante) 
                
                if chave_medicamento not in medicamentos_vendidos_agregado:
                    medicamentos_vendidos_agregado[chave_medicamento] = {
                        'nome': item_venda.medicamento.nome,
                        'fabricante': item_venda.medicamento.fabricante,
                        'quantidade_total': 0,
                        'valor_total': 0.0
                    }
                
                medicamentos_vendidos_agregado[chave_medicamento]['quantidade_total'] += item_venda.quantidade
                medicamentos_vendidos_agregado[chave_medicamento]['valor_total'] += item_venda.subtotal
        
        lista_medicamentos_ordenada = list(medicamentos_vendidos_agregado.values())

        lista_medicamentos_ordenada.sort(key=lambda x: x['quantidade_total'], reverse=True)

        if not lista_medicamentos_ordenada:
            self.__tela_relatorio.mostra_msg("Nenhum medicamento foi vendido no período selecionado.")
            return
        
        self.__tela_relatorio.mostra_msg("\n--- Medicamentos Mais Vendidos no Período ---")
        for i, dados_medicamento in enumerate(lista_medicamentos_ordenada):
            self.__tela_relatorio.mostra_msg(
                f"{i + 1}. Medicamento: {dados_medicamento['nome']} | "
                f"Fabricante: {dados_medicamento['fabricante']} | "
                f"Quantidade total: {dados_medicamento['quantidade_total']} | "
                f"Valor total: R$ {dados_medicamento['valor_total']:.2f}"
            )
        self.__tela_relatorio.mostra_msg("------------------------------------------")

        

    def clientes_que_mais_compraram(self):
        self.__tela_relatorio.mostra_msg(">> Relatório de Clientes que mais Compraram")
        self.__tela_relatorio.mostra_msg("Selecione o período desejado:")
        
        data_inicio, data_fim = self.__tela_relatorio.pega_periodo()

        vendas_do_periodo = self.__controlador_sistema.controlador_venda.get_vendas_por_periodo(data_inicio, data_fim)

        clientes_com_compras = {}

        for venda in vendas_do_periodo:
            cpf_cliente = venda.cliente.cpf
            nome_cliente = venda.cliente.nome

            if cpf_cliente not in clientes_com_compras:
                clientes_com_compras[cpf_cliente] = {
                    'nome': nome_cliente,
                    'quantidade_total': 0,
                    'valor_total': 0.0
                }
            
            for item_venda in venda.itens:
                clientes_com_compras[cpf_cliente]['quantidade_total'] += item_venda.quantidade
            
            clientes_com_compras[cpf_cliente]['valor_total'] += venda.valor_total()
        
        lista_clientes_ordenada = list(clientes_com_compras.values())

        lista_clientes_ordenada.sort(key=lambda x: x["quantidade_total"], reverse=True)

        if not lista_clientes_ordenada:
            self.__tela_relatorio.mostra_msg("Nenhum cliente realizou compras no período selecionado.")
            return

        self.__tela_relatorio.mostra_msg("\n--- Clientes que Mais Compraram no Período ---")
        for i, dados_compra in enumerate(lista_clientes_ordenada):
            self.__tela_relatorio.mostra_msg(
                f"{i + 1}. Cliente: {dados_compra['nome']} | "
                f"Quantidade total de produtos: {dados_compra['quantidade_total']} | "
                f"Valor total: R$ {dados_compra['valor_total']:.2f}"
            )
        self.__tela_relatorio.mostra_msg("------------------------------------------")


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.vendas_por_periodo,
            2: self.medicamentos_mais_vendidos,
            3: self.clientes_que_mais_compraram,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_relatorio.tela_opcoes()
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
