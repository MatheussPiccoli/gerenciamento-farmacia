from limite.tela_relatorios import TelaRelatorios
from datetime import datetime, date, timedelta

class RelatorioController:
    def __init__(self, controlador_sistema):
        self.__tela_relatorio = TelaRelatorios()
        self.__controlador_sistema = controlador_sistema

    def obter_periodo(self):
        escolha = self.__tela_relatorio.seleciona_periodo_rapido()
        hoje = date.today()
        if escolha == '1':
            return hoje - timedelta(days=30), hoje
        elif escolha == '2':
            return hoje - timedelta(days=90), hoje
        elif escolha == '3':
            return hoje - timedelta(days=180), hoje
        elif escolha == '4':
            return hoje - timedelta(days=365), hoje
        elif escolha == '5':
            return self.__tela_relatorio.pega_periodo()
        else:
            return None, None

    def vendas_por_periodo(self):
        data_inicio, data_fim = self.obter_periodo()
        if not data_inicio or not data_fim:
            self.__tela_relatorio.mostra_msg("Operação cancelada.")
            return
        vendas = self.__controlador_sistema.controlador_venda.get_vendas_por_periodo(data_inicio, data_fim)
        vendas_filtradas = [venda for venda in vendas if data_inicio <= venda.data <= data_fim]
        if not vendas_filtradas:
            self.__tela_relatorio.mostra_msg("Nenhuma venda encontrada nesse período.")
            return
        lista_vendas = []
        for venda in vendas_filtradas:
            lista_vendas.append({
                "cliente": venda.cliente.nome,
                "farmaceutico": venda.farmaceutico.nome,
                "data": venda.data.strftime("%d/%m/%Y"),
                "itens": venda.itens
            })
        self.__tela_relatorio.mostra_lista_vendas(lista_vendas)

    def medicamentos_mais_vendidos(self):
        data_inicio, data_fim = self.obter_periodo()
        if not data_inicio or not data_fim:
            self.__tela_relatorio.mostra_msg("Operação cancelada.")
            return
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
        ranking = lista_medicamentos_ordenada[:10]
        self.__tela_relatorio.mostra_ranking_medicamentos(ranking)

    def clientes_que_mais_compraram(self):
        data_inicio, data_fim = self.obter_periodo()
        if not data_inicio or not data_fim:
            self.__tela_relatorio.mostra_msg("Operação cancelada.")
            return
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
        lista_clientes_ordenada.sort(key=lambda x: x["valor_total"], reverse=True)
        ranking = lista_clientes_ordenada[:10]
        self.__tela_relatorio.mostra_ranking_clientes(ranking)

    def melhores_vendedores(self):
        data_inicio, data_fim = self.obter_periodo()
        if not data_inicio or not data_fim:
            self.__tela_relatorio.mostra_msg("Operação cancelada.")
            return
        vendas_do_periodo = self.__controlador_sistema.controlador_venda.get_vendas_por_periodo(data_inicio, data_fim)
        vendedores = {}
        for venda in vendas_do_periodo:
            cpf_farm = venda.farmaceutico.cpf
            nome_farm = venda.farmaceutico.nome
            if cpf_farm not in vendedores:
                vendedores[cpf_farm] = {
                    'nome': nome_farm,
                    'cpf': cpf_farm,
                    'qtd_vendas': 0,
                    'valor_total': 0.0
                }
            vendedores[cpf_farm]['qtd_vendas'] += 1
            vendedores[cpf_farm]['valor_total'] += venda.valor_total()
        ranking = sorted(vendedores.values(), key=lambda x: x['valor_total'], reverse=True)[:10]
        self.__tela_relatorio.mostra_ranking_vendedores(ranking)

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
