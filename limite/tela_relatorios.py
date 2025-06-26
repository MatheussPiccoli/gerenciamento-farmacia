import PySimpleGUI as sg
from datetime import datetime, date

class TelaRelatorios():
    def tela_opcoes(self):
        layout = [
            [sg.Text('-------- Relatórios --------', font=('Any', 16))],
            [sg.Button('1 - Vendas por Período', key='1')],
            [sg.Button('2 - Medicamentos mais Vendidos', key='2')],
            [sg.Button('3 - Clientes que mais Compraram', key='3')],
            [sg.Button('4 - Melhores Vendedores', key='4')],
            [sg.Button('0 - Retornar', key='0')]
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
        linhas = []
        for venda in lista_vendas:
            itens = ''
            if venda["itens"]:
                for item in venda["itens"]:
                    itens += f"  - Medicamento: {item.medicamento.nome} | Quantidade: {item.quantidade} | Subtotal: R$ {item.subtotal:.2f}\n"
            else:
                itens = '  Nenhum item registrado para esta venda.'
            linhas.append(f"Cliente: {venda['cliente']} | Farmacêutico: {venda['farmaceutico']} | Data: {venda['data']}\nItens:\n{itens}\n")
        layout = [
            [sg.Text('Vendas Encontradas:')],
            [sg.Multiline('\n'.join(linhas), size=(80, min(20, len(linhas)*4)), disabled=True)],
            [sg.Button('OK')]
        ]
        window = sg.Window('Vendas por Período', layout)
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

        