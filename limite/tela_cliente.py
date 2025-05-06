
class TelaCliente():
  def tela_opcoes(self):
    print("-------- clienteS ----------")
    print("Escolha a opcao")
    print("1 - Incluir cliente")
    print("2 - Alterar cliente")
    print("3 - Listar clientes")
    print("4 - Excluir cliente")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_cliente(self):
    print("-------- DADOS cliente ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    return {"nome": nome, "telefone": telefone, "cpf": cpf}

  def mostra_cliente(self, dados_cliente):
    print("NOME DO cliente: ", dados_cliente["nome"])
    print("FONE DO cliente: ", dados_cliente["telefone"])
    print("CPF DO cliente: ", dados_cliente["cpf"])
    print("\n")

  def seleciona_cliente(self):
    cpf = input("CPF do cliente que deseja selecionar: ")
    return cpf

  def mostra_mensagem(self, msg):
    print(msg)