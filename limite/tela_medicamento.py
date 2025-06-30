import PySimpleGUI as sg

class TelaMedicamento():
    def tela_opcoes(self):
        layout = [
            [sg.Text('-------- Medicamentos --------', font=('Helvica', 20))],
            [sg.Button('Registrar Medicamento', key='1')],
            [sg.Button('Alterar ou Excluir Medicamento', key='2')],
            [sg.Button('Listar Medicamentos', key='3')],
            [sg.Button('Retornar', key='0')]
        ]
        window = sg.Window('Menu Medicamentos', layout)
        opcao = None
        while True:
            event, _ = window.read()
            if event in ['0', sg.WIN_CLOSED]:
                opcao = 0
                break
            elif event in ['1', '2', '3']:
                opcao = int(event)
                break
        window.close()
        return opcao

    def pega_dados_medicamento(self):
        layout = [
            [sg.Text('-------- Dados Medicamento --------', font=('Any', 14))],
            [sg.Text('Nome:'), sg.Input(key='nome')],
            [sg.Text('Fabricante:'), sg.Input(key='fabricante')],
            [sg.Text('Preço:'), sg.Input(key='preco')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Cadastro de Medicamento', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None
            try:
                preco = float(values['preco'])
                if preco == 0:
                    window.close()
                    return None
                dados = {"nome": values['nome'], "fabricante": values['fabricante'], "preco": preco}
                window.close()
                return dados
            except (ValueError, TypeError):
                sg.popup('Preço inválido. Por favor, digite um número real ou cancele a operação (0 para cancelar).')

    def mostra_medicamento(self, dados_medicamento):
        msg = f"Nome: {dados_medicamento['nome']}\nFabricante: {dados_medicamento['fabricante']}\nPreço: {dados_medicamento['preco']}"
        sg.popup(msg, title='Medicamento')

    def pede_nome_medicamento(self):
        layout = [
            [sg.Text('Digite o nome do medicamento:')],
            [sg.Input(key='nome')],
            [sg.Button('OK')]
        ]
        window = sg.Window('Buscar Medicamento', layout)
        event, values = window.read()
        window.close()
        return values['nome'] if event == 'OK' else None

    def mostra_opcoes_medicamentos(self, lista_medicamentos):
        opcoes = [f"{idx+1} - Fabricante: {med.fabricante}" for idx, med in enumerate(lista_medicamentos)]
        sg.popup("Vários medicamentos encontrados com esse nome:\n" + "\n".join(opcoes), title='Escolha Medicamento')

    def pede_opcao_medicamento(self, total_opcoes):
        layout = [
            [sg.Text(f'Digite o número do medicamento desejado (1 a {total_opcoes}):')],
            [sg.Input(key='opcao')],
            [sg.Button('OK')]
        ]
        window = sg.Window('Escolher Medicamento', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                return None
            try:
                opcao = int(values['opcao'])
                if 1 <= opcao <= total_opcoes:
                    window.close()
                    return opcao
                else:
                    sg.popup('Número fora do intervalo.')
            except (ValueError, TypeError):
                sg.popup('Entrada inválida. Digite um número inteiro.')

    def mostra_opcoes_de_acao(self):
        layout = [
            [sg.Text('O que deseja fazer com o medicamento selecionado?')],
            [sg.Button('1 - Alterar medicamento', key='1')],
            [sg.Button('2 - Excluir medicamento', key='2')],
            [sg.Button('0 - Cancelar', key='0')]
        ]
        window = sg.Window('Ação Medicamento', layout)
        while True:
            event, _ = window.read()
            if event in ['0', sg.WIN_CLOSED]:
                window.close()
                return 0
            elif event in ['1', '2']:
                window.close()
                return int(event)

    def mostra_msg(self, msg):
        sg.popup(msg)

    def mostra_lista_medicamentos(self, lista_medicamentos):
        if not lista_medicamentos:
            sg.popup('Nenhum medicamento cadastrado.')
            return
        linhas = []
        for med in lista_medicamentos:
            linhas.append(f"Nome: {med.nome} | Fabricante: {med.fabricante} | Preço: {med.preco}")
        layout = [
            [sg.Text('Lista de Medicamentos:')],
            [sg.Multiline('\n'.join(linhas), size=(60, min(20, len(linhas))), disabled=True)],
            [sg.Button('OK')]
        ]
        window = sg.Window('Medicamentos Cadastrados', layout)
        window.read()
        window.close()
