import PySimpleGUI as sg

class TelaSistema:
    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkGreen3')
        layout = [
            [sg.Text("-------- SISTEMA DE FARMÁCIA ----------", font=('Helvica', 20))],
            [sg.Text("Escolha a opção", font=('Helvica', 14))],
            [sg.Radio("Clientes", "opcoes", key='1')],
            [sg.Radio("Farmacêuticos", "opcoes", key='2')],
            [sg.Radio("Vendas", "opcoes", key='3')],
            [sg.Radio("Estoque", "opcoes", key='4')],
            [sg.Radio("Medicamentos", "opcoes", key='5')],
            [sg.Radio("Relatórios", "opcoes", key='6')],
            [sg.Radio("Finalizar sistema", "opcoes", key='0')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('Menu do Sistema', layout)
        
        while True:
            event, values = window.read()
            
            if event in [sg.WIN_CLOSED, 'Cancelar']:
                window.close()
                return 0
            
            if event == 'OK':
                # Verifica qual radio button foi selecionado
                for key, selected in values.items():
                    if selected and key in ['0', '1', '2', '3', '4', '5', '6']:
                        window.close()
                        return int(key)
                
                # Se nenhuma opção foi selecionada
                sg.popup('Por favor, selecione uma opção!')
                
        window.close()
        return 0

    def mostra_mensagem(self, msg):
        sg.popup(msg)
