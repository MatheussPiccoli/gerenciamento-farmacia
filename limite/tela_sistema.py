import PySimpleGUI as sg

class TelaSistema:
    def tela_opcoes(self):
        layout = [
            [sg.Text('-------- Sistema ---------', font=('Any', 16))],
            [sg.Text('Escolha sua opção', font=('Any', 12))],
            [sg.Button('1 - Clientes', key='1')],
            [sg.Button('2 - Farmaceuticos', key='2')],
            [sg.Button('3 - Venda', key='3')],
            [sg.Button('4 - Estoque', key='4')],
            [sg.Button('5 - Medicamentos', key='5')],
            [sg.Button('6 - Relatórios', key='6')],
            [sg.Button('0 - Finalizar sistema', key='0')]
        ]
        window = sg.Window('Menu do Sistema', layout)
        opcao = None
        while True:
            event, _ = window.read()
            if event in ['0', sg.WIN_CLOSED]:
                opcao = 0
                break
            elif event in ['1', '2', '3', '4', '5', '6']:
                opcao = int(event)
                break
        window.close()
        return opcao