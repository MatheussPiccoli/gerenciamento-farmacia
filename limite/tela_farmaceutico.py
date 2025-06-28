import PySimpleGUI as sg


class TelaFarmaceutico():

    def tela_opcoes(self):
        layout = [
                [sg.Text("-------- FARMACEUTICO ----------", font=('Any', 16))],
                [sg.Text("Escolha a opção", font=('Any', 14))],
                [sg.Button("1 - Incluir farmaceutico", key='1')],
                [sg.Button("2 - Alterar farmaceutico", key='2')],
                [sg.Button("3 - Listar farmaceuticos", key='3')],
                [sg.Button("4 - Excluir farmaceutico", key='4')],
                [sg.Button("0 - Retornar", key='0')],
        ]
        window = sg.window('Menu Farmaceuticos', layout)
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

    def pega_dados_farmaceutico(self):
        layout = [
            [sg.Text("-------- Dados Farmaceutico --------", font=('Any', 14))],
            [sg.Text("Nome: "), sg.Input(key='nome')],
            [sg.Text("CPF (somente números, 11 dígitos): "), sg.Input(key='cpf')],
            [sg.Text("salario (somente números, mínimo 8 dígitos): "), sg.Input(key='salario')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('Cadastro de Farmaceutico', layout)
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
            
            salario = self.__pede_salario_validado(values['salario'])
            
            if nome and cpf and salario is not None:
                window.close()
                return {"nome": nome, "cpf": cpf, "salario": salario}
            else:
                sg.popup('Todos os campos são obrigatórios. Por favor, preencha corretamente.')

    def mostra_farmaceutico(self, dados_farmaceutico):
         msg = f"Nome: {dados_farmaceutico['nome']}\nCPF: {dados_farmaceutico['cpf']}\nTelefone: {dados_farmaceutico['telefone']}"
         sg.popup(msg, title='farmaceutico')

    def seleciona_farmaceutico(self):
        layout = [
            [sg.Text("Selecione o CPF do farmaceutico:")],
            [sg.Input(key='cpf')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('Selecionar Farmaceutico', layout)
        event, values = window.read()
        window.close()
        return values['cpf'] if event == 'OK' else None
    
    def mostra_mensagem(self, msg):
        print(msg)

    def __pede_cpf_validado(self, prompt: str) -> str | None:
        sg.popup('Digite o CPF do farmaceutico (somente números, 11 dígitos). Digite "0" para não informar.')
        while True:
            entrada = input(prompt).strip()
            if entrada == '0':
                return None
            
            if entrada.isdigit() and len(entrada) == 11:
                return entrada
            else:
                self.mostra_mensagem("CPF inválido. Deve conter apenas números e ter 11 dígitos. Digite '0' para não informar.")

    def __pede_salario_validado(self, prompt: str) -> float | None:
        sg.popup('Digite o salário do farmaceutico (número real, mínimo 0). Digite "0" para cancelar.')
        while True:
            entrada = input(prompt).strip()
            if entrada.lower() == '0':
                return None
            try:
                salario = float(entrada)
                if salario >= 0:
                    return salario
                else:
                    self.mostra_mensagem("Salário não pode ser negativo. Digite um valor válido.")
            except ValueError:
                self.mostra_mensagem("Salário inválido. Digite um número. Digite '0' para cancelar.")