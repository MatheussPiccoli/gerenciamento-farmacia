import PySimpleGUI as sg
from datetime import datetime

class TelaEstoque():

    def tela_opcoes(self):
        layout = [
                [sg.Text("------ Estoque ------", font=('Helvica', 20))],
                [sg.Button("Listar Estoque", key='1')],
                [sg.Button("Aumentar Estoque (Adicionar Lote)", key='2')],
                [sg.Button("Baixar Estoque", key='3')],
                [sg.Button("Verificar Estoque Baixo", key='4')],
                [sg.Button("Listar Lotes Vencidos", key='5')],
                [sg.Button("Listar Lotes Próximos ao Vencimento", key='6')],
                [sg.Button("Retornar", key='0')],
        ]
        window = sg.Window('Menu Estoque', layout)
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
    
    def pega_dados_lote(self):
        layout =[
            [sg.Text("------ Dados do Lote ------", font=('Any', 14))],
            [sg.Text("Número do Lote: "), sg.Input(key='lote_str')],
            [sg.Text("Validade do lote (DD/MM/AAAA): "), sg.Input(key='validade')],
            [sg.Text("Quantidade: "), sg.Input(key='quantidade')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('Cadastro de Lote', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None
            try:
                lote = values['lote_str']
                validade_str = values['validade']
                validade = datetime.strptime(validade_str, "%d/%m/%Y").date()
                quantidade = int(values['quantidade'])
                if quantidade <= 0:
                    sg.popup('Quantidade deve ser um número inteiro positivo.')
                    continue
                window.close()
                return {"lote": lote, "validade": validade, "quantidade": quantidade}
            except (ValueError, TypeError):
                sg.popup('Dados inválidos. Por favor, verifique os campos e tente novamente.')

    def pega_quantidade_para_baixa(self):
        sg.popup('Informe a quantidade a ser baixada do estoque:')
        layout = [
            [sg.Text("Quantidade a ser baixada:")],
            [sg.Input(key='quantidade')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window = sg.Window('Baixa de Estoque', layout)
        event, values = window.read()
        window.close()
        return int(values['quantidade']) if event == 'OK' else None 

    def mostra_estoque(self, lotes):
        if not lotes:
            sg.popup('Nenhum lote cadastrado no estoque.')
            return
        linhas = []
        for lote in lotes:
            linhas.append(f"Medicamento: {lote.medicamento.nome} | Lote: {lote.lote} | Validade: {lote.validade} | Quantidade: {lote.quantidade}")
        window = sg.Window('Estoque', [[sg.Text('\n'.join(linhas))]])
        window.read()
        window.close()
    
    def mostra_lote(self, lote):
        msg = f"Medicamento: {lote.medicamento.nome}\nLote: {lote.lote}\nValidade: {lote.validade}\nQuantidade: {lote.quantidade}"
        sg.popup(msg, title='Lote')

    def mostra_mensagem(self, msg):
        print(msg)
