import PySimpleGUI as sg

class TelaCliente():
    def tela_opcoes(self):
        layout = [
                [sg.Text("-------- CLIENTES ----------", font=('Helvica', 20))],
                [sg.Text("Escolha a opção", font=('Helvica', 14))],
                [sg.Button("Incluir cliente", key='1')],
                [sg.Button("Alterar cliente", key='2')],
                [sg.Button("Listar clientes", key='3')],
                [sg.Button("Excluir cliente", key='4')],
                [sg.Button("Retornar", key='0')],
        ]
        window = sg.Window('Menu Clientes', layout)
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
            [sg.Text("-------- Dados Cliente --------", font=('Helvica', 14))],
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
            cpf = self.__valida_cpf(values['cpf'].strip())
            if cpf is None:
                sg.popup('CPF inválido. Deve conter apenas números e ter 11 dígitos.')
                continue
            
            telefone = self.__valida_telefone(values['telefone'].strip())
            if telefone is None:
                sg.popup('Telefone inválido. Deve conter apenas números e ter no mínimo 8 dígitos.')
                continue
            
            if nome and cpf and telefone:
                window.close()
                return {"nome": nome, "cpf": cpf, "telefone": telefone}
            else:
                sg.popup('Todos os campos são obrigatórios. Por favor, preencha corretamente.')

    def __valida_cpf(self, cpf: str) -> str | None:
        if cpf and cpf.isdigit() and len(cpf) == 11:
            return cpf
        return None

    def __valida_telefone(self, telefone: str) -> str | None:
        if telefone and telefone.isdigit() and len(telefone) >= 8:
            return telefone
        return None

    def mostra_cliente(self, dados_cliente):
        msg = f"Nome: {dados_cliente['nome']}\nCPF: {dados_cliente['cpf']}\nTelefone: {dados_cliente['telefone']}"
        sg.popup(msg, title='Cliente')

    def mostra_clientes(self, lista_clientes):
        if not lista_clientes:
            sg.popup("Nenhum cliente cadastrado.")
            return
        
        dados = []
        for cliente in lista_clientes:
            dados.append([cliente['nome'], cliente['cpf'], cliente['telefone']])
        
        layout = [
            [sg.Text("Lista de Clientes Cadastrados", font=('Helvica', 16))],
            [sg.Table(values=dados, 
                     headings=['Nome', 'CPF', 'Telefone'], 
                     auto_size_columns=True,
                     display_row_numbers=False,
                     justification='left',
                     num_rows=min(len(dados), 10))],
            [sg.Button("OK")]
        ]
        
        window = sg.Window('Clientes Cadastrados', layout)
        window.read()
        window.close()

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
        sg.popup(msg)