import PySimpleGUI as sg
from datetime import datetime, date

class TelaRelatorios():
    def tela_opcoes(self):
        layout = [
            [sg.Text('-------- Relatórios --------', font=('Helvica', 20))],
            [sg.Button('Vendas por Período', key='1')],
            [sg.Button('Medicamentos mais Vendidos', key='2')],
            [sg.Button('Clientes que mais Compraram', key='3')],
            [sg.Button('Melhores Vendedores', key='4')],
            [sg.Button('Retornar', key='0')]
        ]
        window = sg.Window('Menu Relatórios', layout)
        opcao = None
        while True:
            event, _ = window.read()
            if event in ['0', sg.WIN_CLOSED]:
                opcao = 0
                break
            elif event in ['1', '2', '3', '4']:
                opcao = int(event)
                break
        window.close()
        return opcao

    def pega_periodo(self):
        layout = [
            [sg.Text('Informe o período para o relatório:', font=('Any', 14))],
            [sg.Text('Data de início (dd/mm/aaaa):'), sg.Input(key='data_inicio')],
            [sg.Text('Data de fim (dd/mm/aaaa):'), sg.Input(key='data_fim')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Período do Relatório', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None, None
            try:
                data_inicio = datetime.strptime(values['data_inicio'], "%d/%m/%Y").date()
                data_fim = datetime.strptime(values['data_fim'], "%d/%m/%Y").date()
                if data_inicio > data_fim:
                    sg.popup('A data de início não pode ser maior que a data de fim.')
                    continue
                window.close()
                return data_inicio, data_fim
            except (ValueError, TypeError):
                sg.popup('Formato de data inválido. Por favor, use o formato dd/mm/aaaa.')

    def seleciona_periodo_rapido(self):
        layout = [
            [sg.Text('Selecione o período para o relatório:', font=('Any', 14))],
            [sg.Button('Último mês', key='1')],
            [sg.Button('Últimos 3 meses', key='2')],
            [sg.Button('Últimos 6 meses', key='3')],
            [sg.Button('Último ano', key='4')],
            [sg.Button('Selecionar período manualmente', key='5')],
            [sg.Button('Cancelar', key='0')]
        ]
        window = sg.Window('Escolher Período', layout)
        while True:
            event, _ = window.read()
            window.close()
            return event

    def mostra_venda(self, dados_venda):
        itens = ''
        if dados_venda["itens"]:
            for item in dados_venda["itens"]:
                itens += f"  - Medicamento: {item.medicamento.nome} | Quantidade: {item.quantidade} | Subtotal: R$ {item.subtotal:.2f}\n"
        else:
            itens = '  Nenhum item registrado para esta venda.'
        msg = f"Cliente: {dados_venda['cliente']}\nFarmacêutico: {dados_venda['farmaceutico']}\nData: {dados_venda['data']}\nItens da Venda:\n{itens}"
        sg.popup(msg, title='Venda')

    def mostra_lista_vendas(self, lista_vendas):
        if not lista_vendas:
            sg.popup('Nenhuma venda encontrada para o período.')
            return
        linhas = ["LISTAGEM DE VENDAS POR PERÍODO", ""]
        for venda in lista_vendas:
            linhas.append("="*60)
            linhas.append(f"Cliente: {venda['cliente']} | Farmacêutico: {venda['farmaceutico']} | Data: {venda['data']}")
            linhas.append("Itens:")
            if venda["itens"]:
                for item in venda["itens"]:
                    linhas.append(f"   - Medicamento: {item.medicamento.nome} | Quantidade: {item.quantidade} | Subtotal: R$ {item.subtotal:.2f}")
            else:
                linhas.append('   Nenhum item registrado para esta venda.')
            linhas.append("")
        layout = [
            [sg.Text('Vendas Encontradas', font=('Helvica', 16, 'bold'))],
            [sg.Multiline('\n'.join(linhas), size=(80, min(20, len(linhas)*2)), font=('Consolas', 12), disabled=True, autoscroll=True)],
            [sg.Button('OK')]
        ]
        window = sg.Window('Vendas por Período', layout, resizable=True, finalize=True)
        window.read()
        window.close()

    def mostra_lista_generica(self, titulo, linhas):
        if not linhas:
            sg.popup(f'Nenhum dado encontrado para {titulo}.')
            return
        layout = [
            [sg.Text(titulo)],
            [sg.Multiline('\n'.join(linhas), size=(80, min(20, len(linhas)*2)), disabled=True)],
            [sg.Button('OK')]
        ]
        window = sg.Window(titulo, layout)
        window.read()
        window.close()

    def mostra_msg(self, msg):
        sg.popup(msg)

    def mostra_ranking_medicamentos(self, ranking: list[dict]):
        if not ranking:
            sg.popup('Nenhum medicamento vendido no período.')
            return
        linhas = ["RANKING - Medicamentos Mais Vendidos", ""]
        for i, med in enumerate(ranking, 1):
            linhas.append(f"{i:2d}. {med['nome']} ({med['fabricante']}) | Unidades vendidas: {med['quantidade_total']} | Total gerado: R$ {med['valor_total']:.2f}")
        layout = [
            [sg.Text('Medicamentos Mais Vendidos', font=('Helvica', 16, 'bold'))],
            [sg.Multiline('\n'.join(linhas), size=(80, min(15, len(linhas)+2)), font=('Consolas', 12), disabled=True, autoscroll=True)],
            [sg.Button('OK')]
        ]
        window = sg.Window('Ranking de Medicamentos', layout, resizable=True, finalize=True)
        window.read()
        window.close()

    def mostra_ranking_clientes(self, ranking: list[dict]):
        if not ranking:
            sg.popup('Nenhum cliente realizou compras no período.')
            return
        linhas = ["RANKING - Clientes que Mais Compraram", ""]
        for i, cli in enumerate(ranking, 1):
            linhas.append(f"{i:2d}. {cli['nome']} | Produtos comprados: {cli['quantidade_total']} | Total gasto: R$ {cli['valor_total']:.2f}")
        layout = [
            [sg.Text('Clientes que Mais Compraram', font=('Helvica', 16, 'bold'))],
            [sg.Multiline('\n'.join(linhas), size=(80, min(15, len(linhas)+2)), font=('Consolas', 12), disabled=True, autoscroll=True)],
            [sg.Button('OK')]
        ]
        window = sg.Window('Ranking de Clientes', layout, resizable=True, finalize=True)
        window.read()
        window.close()

    def mostra_ranking_vendedores(self, ranking: list[dict]):
        if not ranking:
            sg.popup('Nenhum vendedor realizou vendas no período.')
            return
        linhas = ["RANKING - Melhores Vendedores", ""]
        for i, vend in enumerate(ranking, 1):
            linhas.append(f"{i:2d}. {vend['nome']} (CPF: {vend['cpf']}) | Vendas: {vend['qtd_vendas']} | Total vendido: R$ {vend['valor_total']:.2f}")
        layout = [
            [sg.Text('Melhores Vendedores', font=('Helvica', 16, 'bold'))],
            [sg.Multiline('\n'.join(linhas), size=(80, min(15, len(linhas)+2)), font=('Consolas', 12), disabled=True, autoscroll=True)],
            [sg.Button('OK')]
        ]
        window = sg.Window('Ranking de Vendedores', layout, resizable=True, finalize=True)
        window.read()
        window.close()

        