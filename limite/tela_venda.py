# limite/tela_venda.py
from datetime import datetime

class TelaVenda():

    def tela_opcoes(self):
        print("------ Vendas ------")
        print("1 - Registrar Nova Venda")
        print("2 - Alterar Venda Existente")
        print("3 - Listar Todas as Vendas")
        print("4 - Excluir Venda")
        print("0 - Retornar")
        try:
            return int(input("Escolha a opção: "))
        except ValueError:
            print("Opção inválida. Digite um número inteiro.")
            return -1

    def pega_dados_item(self):
        print("\n--- Adicionar Item à Venda ---")
        try:
            nome_medicamento = input("Nome do medicamento (ou 'sair' para finalizar adição de itens): ").strip()
            if nome_medicamento.lower() == 'sair':
                return None

            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser um número positivo.")

            return {"nome": nome_medicamento, "quantidade": quantidade}
        except ValueError as e:
            self.mostra_mensagem(f"Entrada inválida para o item: {e}")
            return None

    def continuar_venda(self):
        while True:
            resposta = input("Deseja adicionar mais itens à venda? (S/N): ").strip().upper()
            if resposta == 'S':
                return True
            elif resposta == 'N':
                return False
            else:
                self.mostra_mensagem("Resposta inválida. Digite 'S' para sim ou 'N' para não.")

    def seleciona_venda(self):
        try:
            id_venda = int(input("Digite o ID da venda para selecionar: "))
            return id_venda
        except ValueError:
            self.mostra_mensagem("ID de venda inválido. Digite um número inteiro.")
            return -1

    def pega_cpf_cliente(self) -> str:
        """Pede o CPF do cliente ao usuário."""
        cpf = input("Digite o CPF do cliente (somente números): ").strip()
        if not cpf.isdigit() or len(cpf) != 11:
            self.mostra_mensagem("CPF inválido. Deve conter 11 dígitos numéricos.")
            return None 
        return cpf

    def pega_cpf_farmaceutico(self) -> str:
        """Pede o CPF do farmacêutico ao usuário."""
        cpf = input("Digite o CPF do farmacêutico (somente números): ").strip()
        if not cpf.isdigit() or len(cpf) != 11:
            self.mostra_mensagem("CPF inválido. Deve conter 11 dígitos numéricos.")
            return None 
        return cpf
        
    def mostra_venda(self, dados_venda: dict):
        print("\n--- Detalhes da Venda ---")
        print(f"ID da Venda: {dados_venda['id']}")
        print(f"Cliente: {dados_venda['cliente_nome']}")
        print(f"Farmacêutico: {dados_venda['farmaceutico_nome']}")
        print(f"Data: {dados_venda['data']}")
        print("Itens:")
        if dados_venda['itens']:
            for item in dados_venda['itens']:
                print(f"  - ID Item: {item['id']} | Medicamento: {item['medicamento_nome']} | Quantidade: {item['quantidade']} | Subtotal: R$ {item['subtotal']:.2f}")
        else:
            print("  Nenhum item nesta venda.")
        print(f"Valor Total: R$ {dados_venda['valor_total']:.2f}")
        print("-------------------------\n")

    def mostra_mensagem(self, msg: str):
        print(msg)