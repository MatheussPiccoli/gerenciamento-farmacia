from Models.cliente import Cliente


class TelaCliente():
  def tela_opcoes(self):
    while True:
      try:
        print("-------- clienteS ----------")
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
          print("Opção Inválida. DIgite um número entre 0 e 4")
      except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro")

  def pega_dados_cliente(self):
    print("-------- Dados cliente ----------")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    id = Cliente.contador_id

    return {"nome": nome, "cpf": cpf, "telefone": telefone, "id": id}

  def mostra_cliente(self, dados_cliente):
    print("Nome do cliente: ", dados_cliente["nome"])
    print("CPF do cliente: ", dados_cliente["cpf"])
    print("Telefone do cliente: ", dados_cliente["telefone"])
    print("ID do cliente: ", dados_cliente["id"])
    print("\n")

  def seleciona_cliente(self):
    cpf = input("CPF do cliente que deseja selecionar: ")
    return cpf

  def mostra_mensagem(self, msg):
    print(msg)