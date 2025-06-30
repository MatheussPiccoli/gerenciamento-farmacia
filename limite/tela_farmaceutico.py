import PySimpleGUI as sg


class TelaFarmaceutico():

    def tela_opcoes(self):
        layout = [
                [sg.Text("-------- FARMACEUTICO ----------", font=('Helvica', 20))],
                [sg.Text("Escolha a opção", font=('Helvica', 14))],
                [sg.Button("Incluir farmaceutico", key='1')],
                [sg.Button("Alterar farmaceutico", key='2')],
                [sg.Button("Listar farmaceuticos", key='3')],
                [sg.Button("Excluir farmaceutico", key='4')],
                [sg.Button("Retornar", key='0')],
        ]
        window = sg.Window('Menu Farmaceuticos', layout)
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
            [sg.Text("-------- Dados Farmaceutico --------", font=('Helvica', 14))],
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
            cpf = self.__valida_cpf(values['cpf'].strip())
            if cpf is None:
                sg.popup('CPF inválido. Deve conter apenas números e ter 11 dígitos.')
                continue
            
            salario = self.__valida_salario(values['salario'].strip())
            if salario is None:
                sg.popup('Salário inválido. Deve ser um número positivo.')
                continue
            
            if nome and cpf and salario is not None:
                window.close()
                return {"nome": nome, "cpf": cpf, "salario": salario}
            else:
                sg.popup('Todos os campos são obrigatórios. Por favor, preencha corretamente.')

    def mostra_farmaceutico(self, dados_farmaceutico):
         msg = f"Nome: {dados_farmaceutico['nome']}\nCPF: {dados_farmaceutico['cpf']}\nTelefone: {dados_farmaceutico['telefone']}"
         sg.popup(msg, title='farmaceutico')

    def mostra_farmaceuticos(self, lista_farmaceuticos):
        if not lista_farmaceuticos:
            sg.popup("Nenhum farmacêutico cadastrado.")
            return
        
        dados = []
        for farmaceutico in lista_farmaceuticos:
            dados.append([farmaceutico['nome'], farmaceutico['cpf'], f"R$ {farmaceutico['salario']:.2f}"])
        
        layout = [
            [sg.Text("Lista de Farmacêuticos Cadastrados", font=('Helvica', 16))],
            [sg.Table(values=dados, 
                     headings=['Nome', 'CPF', 'Salário'], 
                     auto_size_columns=True,
                     display_row_numbers=False,
                     justification='left',
                     num_rows=min(len(dados), 10))],
            [sg.Button("OK")]
        ]
        
        window = sg.Window('Farmacêuticos Cadastrados', layout)
        window.read()
        window.close()

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
        sg.popup(msg)

    def __valida_cpf(self, cpf: str) -> str | None:
        if cpf and cpf.isdigit() and len(cpf) == 11:
            return cpf
        return None

    def __valida_salario(self, salario: str) -> float | None:
        try:
            valor = float(salario.replace(',', '.'))
            if valor >= 0:
                return valor
        except ValueError:
            pass
        return None