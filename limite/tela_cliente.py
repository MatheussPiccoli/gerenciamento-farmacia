

class TelaCliente():
    def tela_opcoes(self):
        while True:
            try:
                print("-------- CLIENTES ----------")
                print("Escolha a opção")
                print("1 - Incluir cliente")
                print("2 - Alterar cliente")
                print("3 - Listar clientes")
                print("4 - Excluir cliente")
                print("0 - Retornar")

                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    self.mostra_mensagem("Opção Inválida. Digite um número entre 0 e 4")
            except ValueError:
                self.mostra_mensagem("Entrada inválida. Por favor, digite um número inteiro")

    def pega_dados_cliente(self):
        print("-------- Dados Cliente ----------")
        nome = input("Nome: ")
        cpf = self.__pede_cpf_validado("CPF (somente números, 11 dígitos): ")
        if cpf is None:
            self.mostra_mensagem("Operação cancelada.")
            return None
        
        telefone = self.__pede_telefone_validado("Telefone (somente números, ex: 11987654321, ou digite 0 para não informar): ")
        
        return {"nome": nome, "cpf": cpf, "telefone": telefone}

    def __pede_cpf_validado(self, prompt: str) -> str | None:
        while True:
            entrada = input(prompt).strip()
            if entrada == '0':
                return None
            
            if entrada.isdigit() and len(entrada) == 11:
                return entrada
            else:
                self.mostra_mensagem("CPF inválido. Deve conter exatamente 11 dígitos numéricos. Digite '0' para cancelar.")

    def __pede_telefone_validado(self, prompt: str) -> str:
        while True:
            entrada = input(prompt).strip()
            if entrada == '0':
                return ""
            
            if entrada.isdigit() and len(entrada) >= 8:
                return entrada
            else:
                self.mostra_mensagem("Telefone inválido. Deve conter apenas números e ter pelo menos 8 dígitos. Digite '0' para não informar.")

    def mostra_cliente(self, dados_cliente):
        print("Nome do cliente: ", dados_cliente["nome"])
        print("CPF do cliente: ", dados_cliente["cpf"])
        print("Telefone do cliente: ", dados_cliente["telefone"])
        print("\n")

    def seleciona_cliente(self):
        while True:
            cpf = input("CPF do cliente que deseja selecionar (somente números): ").strip()
            if cpf.isdigit() and len(cpf) == 11:
                return cpf
            else:
                self.mostra_mensagem("CPF inválido. Deve conter 11 dígitos numéricos.")

    def mostra_mensagem(self, msg):
        print(msg)