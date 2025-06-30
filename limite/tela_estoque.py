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
            linhas.append(f"ID: {lote.medicamento.id} | Medicamento: {lote.medicamento.nome} | Lote: {lote.lote} | Validade: {lote.validade} | Quantidade: {lote.quantidade}")
        window = sg.Window('Estoque', [[sg.Text('\n'.join(linhas))]])
        window.read()
        window.close()
    
    def mostra_lote(self, lote):
        msg = f"Medicamento: {lote.medicamento.nome}\nLote: {lote.lote}\nValidade: {lote.validade}\nQuantidade: {lote.quantidade}"
        sg.popup(msg, title='Lote')

    def mostra_mensagem(self, msg):
        print(msg)

    def mostra_estoque_baixo(self, lotes_baixos):
        if not lotes_baixos:
            sg.popup('Nenhum medicamento com estoque baixo (quantidade abaixo de 5).')
            return
        linhas = ["MEDICAMENTOS COM ESTOQUE BAIXO", ""]
        for lote in lotes_baixos:
            linhas.append(f"Medicamento: {lote.medicamento.nome} | Lote: {lote.lote} | Validade: {lote.validade} | Quantidade: {lote.quantidade}")
        layout = [
            [sg.Text('Estoque Baixo', font=('Helvica', 16, 'bold'))],
            [sg.Multiline('\n'.join(linhas), size=(80, min(15, len(linhas)+2)), font=('Consolas', 12), disabled=True, autoscroll=True)],
            [sg.Button('OK')]
        ]
        window = sg.Window('Estoque Baixo', layout, resizable=True, finalize=True)
        window.read()
        window.close()

    def mostra_lotes_vencidos(self, lotes_vencidos):
        if not lotes_vencidos:
            sg.popup('Nenhum lote vencido encontrado.')
            return
        linhas = ["LOTES VENCIDOS", ""]
        for lote in lotes_vencidos:
            linhas.append(f"Medicamento: {lote.medicamento.nome} | Lote: {lote.lote} | Validade: {lote.validade} | Quantidade: {lote.quantidade}")
        layout = [
            [sg.Text('Lotes Vencidos', font=('Helvica', 16, 'bold'))],
            [sg.Multiline('\n'.join(linhas), size=(80, min(15, len(linhas)+2)), font=('Consolas', 12), disabled=True, autoscroll=True)],
            [sg.Button('OK')]
        ]
        window = sg.Window('Lotes Vencidos', layout, resizable=True, finalize=True)
        window.read()
        window.close()

    def mostra_lotes_proximos(self, lotes_proximos):
        if not lotes_proximos:
            sg.popup('Nenhum lote próximo ao vencimento encontrado.')
            return
        linhas = ["LOTES PRÓXIMOS AO VENCIMENTO", ""]
        for lote in lotes_proximos:
            linhas.append(f"Medicamento: {lote.medicamento.nome} | Lote: {lote.lote} | Validade: {lote.validade} | Quantidade: {lote.quantidade}")
        layout = [
            [sg.Text('Lotes Próximos ao Vencimento', font=('Helvica', 16, 'bold'))],
            [sg.Multiline('\n'.join(linhas), size=(80, min(15, len(linhas)+2)), font=('Consolas', 12), disabled=True, autoscroll=True)],
            [sg.Button('OK')]
        ]
        window = sg.Window('Lotes Próximos ao Vencimento', layout, resizable=True, finalize=True)
        window.read()
        window.close()
