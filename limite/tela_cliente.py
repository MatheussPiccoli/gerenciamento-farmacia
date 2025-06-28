import PySimpleGUI as sg

class TelaCliente():
    def tela_opcoes(self):
        layout = [
                [sg.Text("-------- CLIENTES ----------", font=('Any', 16))],
                [sg.Text("Escolha a opção", font=('Any', 14))],
                [sg.Button("1 - Incluir cliente", key='1')],
                [sg.Button("2 - Alterar cliente", key='2')],
                [sg.Button("3 - Listar clientes", key='3')],
                [sg.Button("4 - Excluir cliente", key='4')],
                [sg.Button("0 - Retornar", key='0')],
        ]
        window = sg.window('Menu Clientes', layout)
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
               
    def pega_dados_cliente(self):
        layout = [
            [sg.Text("-------- Dados Cliente --------", font=('Any', 14))],
            [sg.Text("Nome: "), sg.Input(key='nome')],
            [sg.Text("CPF (somente números, 11 dígitos): "), sg.Input(key='cpf')],
            [sg.Text("Telefone (somente números, mínimo 8 dígitos): "), sg.Input(key='telefone')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('Cadastro de Cliente', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None
            
            nome = values['nome'].strip()
            cpf = self.__pede_cpf_validado(values['cpf'])
            if cpf is None:
                window.close()
                return None
            
            telefone = self.__pede_telefone_validado(values['telefone'])
            
            if nome and cpf and telefone is not None:
                window.close()
                return {"nome": nome, "cpf": cpf, "telefone": telefone}
            else:
                sg.popup('Todos os campos são obrigatórios. Por favor, preencha corretamente.')

    def __pede_cpf_validado(self, prompt: str) -> str | None:
        sg.popup('Digite o CPF do cliente (somente números, 11 dígitos). Digite "0" para não informar.')
        while True:
            entrada = input(prompt).strip()
            if entrada == '0':
                return None
            
            if entrada.isdigit() and len(entrada) == 11:
                return entrada
            else:
                self.mostra_mensagem("CPF inválido. Deve conter apenas números e ter 11 dígitos. Digite '0' para não informar.")

    def __pede_telefone_validado(self, prompt: str) -> str:
        sg.popup('Digite o telefone do cliente (somente números, mínimo 8 dígitos). Digite "0" para não informar.')
        while True:
            entrada = input(prompt).strip()
            if entrada == '0':
                return None
            
            if entrada.isdigit() and len(entrada) >= 8:
                return entrada
            else:
                self.mostra_mensagem("Telefone inválido. Deve conter apenas números e ter no mínimo 8 dígitos. Digite '0' para não informar.")

    def mostra_cliente(self, dados_cliente):
        msg = f"Nome: {dados_cliente['nome']}\nCPF: {dados_cliente['cpf']}\nTelefone: {dados_cliente['telefone']}"
        sg.popup(msg, title='Cliente')

    def seleciona_cliente(self):
        layout = [
            [sg.Text("Selecione o CPF do cliente:")],
            [sg.Input(key='cpf')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('Selecionar Cliente', layout)
        event, values = window.read()
        window.close()
        return values['cpf'] if event == 'OK' else None

    def mostra_mensagem(self, msg):
        (msg)