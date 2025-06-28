import PySimpleGUI as sg
from datetime import datetime

class TelaVenda():

    def tela_opcoes(self):
        layout = [
            [sg.Text("------ Vendas ------", font=('Any', 16))],
            [sg.Text("Escolha a opção", font=('Any', 14))],
            [sg.Button("1 - Registrar Nova Venda", key='1')],
            [sg.Button("2 - Alterar Venda Existente", key='2')],
            [sg.Button("3 - Listar Todas as Vendas", key='3')],
            [sg.Button("4 - Excluir Venda", key='4')],
            [sg.Button("0 - Retornar", key='0')]
        ]
        window = sg.Window('Menu Vendas', layout)
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

    def pega_dados_item(self):
        layout = [
            [sg.Text("------ Dados do Item ------", font=('Any', 14))],
            [sg.Text("ID do Medicamento:"), sg.Input(key='id_medicamento')],
            [sg.Text("Quantidade:"), sg.Input(key='quantidade')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('Cadastro de Item', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None
            
            try:
                id_medicamento = int(values['id_medicamento'])
                quantidade = int(values['quantidade'])
                if id_medicamento <= 0 or quantidade <= 0:
                    raise ValueError("ID e quantidade devem ser maiores que zero.")
                
                window.close()
                return {"id_medicamento": id_medicamento, "quantidade": quantidade}
            except ValueError as e:
                sg.popup(f"Erro: {e}. Por favor, preencha corretamente.")

    def continuar_venda(self):
        sg.popup("Deseja continuar adicionando itens à venda?", title="Continuar Venda", custom_text=("Sim", "Não"))
        layout = [
            [sg.Text("Deseja continuar adicionando itens à venda?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]
        window = sg.Window('Continuar Venda', layout)
        event, _ = window.read()
        window.close()
        if event == "Sim":
            return True

    def seleciona_venda(self):
        layout = [
            [sg.Text("Selecione o ID da venda:")],
            [sg.Input(key='id_venda')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('Selecionar Venda', layout)
        event, valuer = window.read()
        window.close()  
        return valuer['id_venda'] if event == 'OK' else None

    def pega_cpf_cliente(self) -> str:
        sg.popup('Digite o CPF do cliente (somente números, 11 dígitos). Digite "0" para não informar.')
        while True:
            cpf = input("Digite o CPF do cliente (somente números): ").strip()
            if cpf == '0':
                return None
            if cpf.isdigit() and len(cpf) == 11:
                return cpf
            else:
                self.mostra_mensagem("CPF inválido. Deve conter 11 dígitos numéricos. Digite '0' para não informar.")

    def pega_cpf_farmaceutico(self) -> str:
        sg.popup('Digite o CPF do farmacêutico (somente números, 11 dígitos). Digite "0" para não informar.')
        while True:
            cpf = input("Digite o CPF do farmacêutico (somente números): ").strip()
            if cpf == '0':
                return None
            if cpf.isdigit() and len(cpf) == 11:
                return cpf
            else:
                self.mostra_mensagem("CPF inválido. Deve conter 11 dígitos numéricos. Digite '0' para não informar.")
        
    def mostra_venda(self, dados_venda: dict):
        layout = [
            [sg.Text(f"ID da Venda: {dados_venda['id']}", font=('Any', 14))],
            [sg.Text(f"Cliente: {dados_venda['cliente_nome']}", font=('Any', 12))],
            [sg.Text(f"Farmacêutico: {dados_venda['farmaceutico_nome']}", font=('Any', 12))],
            [sg.Text(f"Data: {dados_venda['data']}", font=('Any', 12))],
            [sg.Text("Itens da Venda:", font=('Any', 12))],
            [sg.Listbox(values=[f"{item['medicamento_nome']} - Qtd: {item['quantidade']} - Subtotal: R$ {item['subtotal']:.2f}" for item in dados_venda['itens']], size=(50, 10), key='itens')],
            [sg.Text(f"Valor Total: R$ {dados_venda['valor_total']:.2f}", font=('Any', 12))],
            [sg.Button("OK")]
        ]
        window = sg.Window('Detalhes da Venda', layout)
        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, 'OK'):
                window.close()
                break

    def mostra_mensagem(self, msg: str):
        (msg)