from Models.farmaceutico import Farmaceutico

class TelaFarmaceutico():

    def tela_opcoes(self):
        while True:
            try:
                print("\n-------- Farmacêutico ----------")
                print("Escolha a opção")
                print("1 - Incluir farmacêutico")
                print("2 - Alterar farmacêutico")
                print("3 - Listar farmacêuticos")
                print("4 - Excluir farmacêutico")
                print("0 - Retornar")

                opcao = int(input("Escolha a opção: "))
                if opcao in [0, 1, 2, 3, 4]:
                    return opcao
                else:
                    self.mostra_mensagem("Opção Inválida. Digite um número entre 0 e 4")
            except ValueError:
                self.mostra_mensagem("Entrada inválida. Por favor, digite um número inteiro.")

    def pega_dados_farmaceutico(self):
        print("-------- Dados Farmacêutico ----------")
        nome = input("Nome: ")
        
        cpf = self.__pede_cpf_validado("CPF (somente números, 11 dígitos): ")
        if cpf is None:
            self.mostra_mensagem("Operação cancelada.")
            return None

        salario = self.__pede_salario_validado("Salário: ")
        if salario is None:
            self.mostra_mensagem("Operação cancelada.")
            return None

        return {"nome": nome, "cpf": cpf, "salario": salario} # Chaves em minúsculas

    def mostra_farmaceutico(self, dados_farmaceutico):
        print("Nome do farmacêutico: ", dados_farmaceutico["nome"])
        print("CPF do farmacêutico: ", dados_farmaceutico["cpf"])
        print("Salário do farmacêutico: ", dados_farmaceutico["salario"])
        print("\n")

    def seleciona_farmaceutico(self):
        while True:
            cpf = input("CPF do farmacêutico que deseja selecionar (somente números): ").strip()
            if cpf.isdigit() and len(cpf) == 11:
                return cpf
            else:
                self.mostra_mensagem("CPF inválido. Deve conter 11 dígitos numéricos.")

    def mostra_mensagem(self, msg):
        print(msg)

    def __pede_cpf_validado(self, prompt: str) -> str | None:
        while True:
            entrada = input(prompt).strip()
            if entrada == '0':
                return None
            
            if entrada.isdigit() and len(entrada) == 11:
                return entrada
            else:
                self.mostra_mensagem("CPF inválido. Deve conter exatamente 11 dígitos numéricos. Digite '0' para cancelar.")

    def __pede_salario_validado(self, prompt: str) -> float | None:
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