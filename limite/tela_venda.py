import PySimpleGUI as sg
from datetime import datetime

class TelaVenda():

    def tela_opcoes(self):
        layout = [
            [sg.Text("------ Vendas ------", font=('Helvica', 20))],
            [sg.Text("Escolha a opção", font=('Helvica', 14))],
            [sg.Button("Registrar Nova Venda", key='1')],
            [sg.Button("Alterar Venda Existente", key='2')],
            [sg.Button("Listar Todas as Vendas", key='3')],
            [sg.Button("Excluir Venda", key='4')],
            [sg.Button("Retornar", key='0')]
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
            [sg.Text("------ Dados do Item ------", font=('Helvica', 14))],
            [sg.Text("Nome do Medicamento:"), sg.Input(key='nome_medicamento')],
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
                nome_medicamento = values['nome_medicamento'].strip()
                quantidade = int(values['quantidade'])
                if not nome_medicamento or quantidade <= 0:
                    raise ValueError("Nome e quantidade devem ser preenchidos corretamente.")
                
                window.close()
                return {"nome": nome_medicamento, "quantidade": quantidade}
            except ValueError as e:
                sg.popup(f"Erro: {e}. Por favor, preencha corretamente.")

    def continuar_venda(self):
        layout = [
            [sg.Text("Deseja continuar adicionando itens à venda?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]
        window = sg.Window('Continuar Venda', layout)
        event, _ = window.read()
        window.close()
        if event == "Sim":
            return True
        return False

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

    def pega_cpf_cliente(self) -> str | None:
        layout = [
            [sg.Text("Digite o CPF do cliente (somente números, 11 dígitos):")],
            [sg.Input(key='cpf')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('CPF do Cliente', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None
            cpf = values['cpf'].strip()
            if cpf.isdigit() and len(cpf) == 11:
                window.close()
                return cpf
            else:
                sg.popup("CPF inválido. Deve conter 11 dígitos numéricos.")

    def pega_cpf_farmaceutico(self) -> str | None:
        layout = [
            [sg.Text("Digite o CPF do farmacêutico (somente números, 11 dígitos):")],
            [sg.Input(key='cpf')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('CPF do Farmacêutico', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None
            cpf = values['cpf'].strip()
            if cpf.isdigit() and len(cpf) == 11:
                window.close()
                return cpf
            else:
                sg.popup("CPF inválido. Deve conter 11 dígitos numéricos.")

    def mostra_venda(self, dados_venda: dict):
        layout = [
            [sg.Text(f"ID da Venda: {dados_venda['id']}", font=('Helvica', 14))],
            [sg.Text(f"Cliente: {dados_venda['cliente_nome']}", font=('Helvica', 12))],
            [sg.Text(f"Farmacêutico: {dados_venda['farmaceutico_nome']}", font=('Helvica', 12))],
            [sg.Text(f"Data: {dados_venda['data']}", font=('Helvica', 12))],
            [sg.Text("Itens da Venda:", font=('Helvica', 12))],
            [sg.Listbox(values=[f"{item['medicamento_nome']} - Qtd: {item['quantidade']} - Subtotal: R$ {item['subtotal']:.2f}" for item in dados_venda['itens']], size=(50, 10), key='itens')],
            [sg.Text(f"Valor Total: R$ {dados_venda['valor_total']:.2f}", font=('Helvica', 12))],
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

    def mostra_lista_vendas(self, lista_vendas: list[dict]):
        if not lista_vendas:
            sg.popup('Nenhuma venda registrada.')
            return
        linhas = []
        for venda in lista_vendas:
            linhas.append("="*60)
            linhas.append(f"ID da Venda: {venda['id']}")
            linhas.append(f"Cliente: {venda['cliente_nome']}")
            linhas.append(f"Farmacêutico: {venda['farmaceutico_nome']}")
            linhas.append(f"Data: {venda['data']}")
            linhas.append(f"Valor Total: R$ {venda['valor_total']:.2f}")
            linhas.append("Itens:")
            for item in venda['itens']:
                linhas.append(f"   - {item['medicamento_nome']} | Qtd: {item['quantidade']} | Subtotal: R$ {item['subtotal']:.2f}")
            linhas.append("")
        layout = [
            [sg.Text('Lista de Vendas', font=('Helvica', 16, 'bold'))],
            [sg.Multiline('\n'.join(linhas), size=(80, 25), font=('Consolas', 12), disabled=True, autoscroll=True, key='ml')],
            [sg.Button('OK')]
        ]
        window = sg.Window('Lista de Vendas', layout, resizable=True, finalize=True)
        window.read()
        window.close()