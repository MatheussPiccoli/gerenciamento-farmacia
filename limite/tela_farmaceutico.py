from Models.farmaceutico import Farmaceutico


class TelaFarmaceutico():
  def tela_opcoes(self):
    print("-------- Farmaceutico ----------")
    print("Escolha a opção")
    print("1 - Incluir farmaceutico")
    print("2 - Alterar farmaceutico")
    print("3 - Listar farmaceuticos")
    print("4 - Excluir farmaceutico")
    print("0 - Retornar")

    opcao = int(input("Escolha a opção: "))
    return opcao

  def pega_dados_farmaceutico(self):
    print("-------- Dados farmaceutico ----------")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    id = Farmaceutico.contador_id
    salario = input("Salario: ")

    return {"Nome": nome, "CPF": cpf, "ID": id, "Salario": salario}

  def mostra_farmaceutico(self, dados_farmaceutico):
    print("Nome do farmaceutico: ", dados_farmaceutico["nome"])
    print("CPF do farmaceutico: ", dados_farmaceutico["cpf"])
    print("ID do farmaceutico: ", dados_farmaceutico["ID"])
    print("Salario do farmaceutico: ", dados_farmaceutico["Salario"])
    print("\n")

  def seleciona_farmaceutico(self):
    cpf = input("CPF do farmaceutico que deseja selecionar: ")
    return cpf

  def mostra_mensagem(self, msg):
    print(msg)