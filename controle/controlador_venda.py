
from limite.tela_venda import TelaVenda
from limite.tela_cliente import TelaCliente
from Models.venda import Venda
from Models.itemvenda import ItemVenda
from controle.exceptions import MedicamentoNaoEncontrado, VendaNaoExistente, EstoqueInsuficiente, ClienteNaoEncontrado, FarmaceuticoNaoEncontrado
from datetime import date
from controle.controlador_cliente import Controladorclientes


class ControladorVenda:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_venda = TelaVenda()
        self.__tela_cliente = TelaCliente()
        self.__vendas = []
        
    def registrar_venda(self):
        itens_venda = []

        while True:
            self.__controlador_sistema.controlador_estoque.listar_estoque()
            dados_item = self.__tela_venda.pega_dados_item()

            if dados_item is None:
                self.__tela_venda.mostra_mensagem("Operação de adicionar item cancelada.")
                break

            try:
                medicamento = self.__controlador_sistema.controlador_medicamento.pega_medicamento_por_nome(dados_item["nome"])
            except MedicamentoNaoEncontrado as erro:
                self.__tela_venda.mostra_mensagem(erro.args[0])
                continue

            quantidade_desejada = dados_item["quantidade"]

            estoque_disponivel = self.__controlador_sistema.controlador_estoque.consultar_total_medicamento(medicamento)


            if estoque_disponivel < quantidade_desejada:
                self.__tela_venda.mostra_mensagem(f"Estoque insuficiente para {medicamento.nome}. Disponível: {estoque_disponivel}")
                continue

            try:
                item_venda = ItemVenda(medicamento=medicamento, quantidade=quantidade_desejada)
                itens_venda.append(item_venda)
                self.__controlador_sistema.controlador_estoque.realizar_baixa_medicamento(medicamento, quantidade_desejada)
                self.__tela_venda.mostra_mensagem(f"Item '{medicamento.nome}' adicionado à venda e estoque baixado.")

            except (EstoqueInsuficiente, ValueError, TypeError) as e:
                self.__tela_venda.mostra_mensagem(f"Erro ao adicionar item ou baixar estoque: {e}. Operação cancelada.")
                return

            if not self.__tela_venda.continuar_venda():
                break

        if not itens_venda:
            self.__tela_venda.mostra_mensagem("Nenhum item foi registrado na venda. Venda cancelada.")
            return

        try:
            self.__controlador_sistema.controlador_cliente.lista_clientes()
            cpf_cliente = self.__tela_venda.pega_cpf_cliente()
            
            if not cpf_cliente:
                self.__tela_venda.mostra_mensagem("CPF do cliente não fornecido. Venda cancelada.")
                return
            
            cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(cpf_cliente)

            if not cliente:
                raise ClienteNaoEncontrado("Cliente não encontrado com o CPF informado. Venda cancelada.")

        except ClienteNaoEncontrado as erro:
            self.__tela_venda.mostra_mensagem(erro.args[0])
            return
        except ValueError:
            self.__tela_venda.mostra_mensagem("CPF de cliente inválido. Venda cancelada.")
            return
        except Exception as erro:
            self.__tela_venda.mostra_mensagem(f"Erro ao selecionar cliente: {erro}. Venda cancelada.")
            return

        try:
            self.__controlador_sistema.controlador_farmaceutico.lista_farmaceuticos()
            cpf_farmaceutico = self.__tela_venda.pega_cpf_farmaceutico()

            if not cpf_farmaceutico:
                self.__tela_venda.mostra_mensagem("CPF do farmacêutico não fornecido. Venda cancelada.")
                return

            farmaceutico = self.__controlador_sistema.controlador_farmaceutico.pega_farmaceutico_por_cpf(cpf_farmaceutico)
            
            if not farmaceutico:
                raise FarmaceuticoNaoEncontrado("Farmacêutico não encontrado com o CPF informado. Venda cancelada.")

        except FarmaceuticoNaoEncontrado as erro:
            self.__tela_venda.mostra_mensagem(erro.args[0])
            return
        except ValueError:
            self.__tela_venda.mostra_mensagem("CPF de farmacêutico inválido. Venda cancelada.")
            return
        except Exception as e:
            self.__tela_venda.mostra_mensagem(f"Erro ao selecionar farmacêutico: {erro}. Venda cancelada.")
            return

        nova_venda = Venda(cliente=cliente, farmaceutico=farmaceutico, data=date.today())
        for item in itens_venda:
            nova_venda.adicionar_item(item)

        self.__vendas.append(nova_venda)
        total = nova_venda.valor_total()

        self.__tela_venda.mostra_mensagem(f"Venda registrada com sucesso! ID da Venda: {nova_venda.id} | Total: R$ {total:.2f}")

    def listar_vendas(self):
        if not self.__vendas:
            self.__tela_venda.mostra_mensagem("Nenhuma venda registrada.")
            return

        for venda in self.__vendas:
            itens_para_tela = []
            for item in venda.itens:
                itens_para_tela.append({
                    "id": item.id,
                    "medicamento_nome": item.medicamento.nome,
                    "quantidade": item.quantidade,
                    "subtotal": item.subtotal
                })

            self.__tela_venda.mostra_venda({
                "id": venda.id,
                "cliente_nome": venda.cliente.nome,
                "farmaceutico_nome": venda.farmaceutico.nome,
                "data": venda.data.strftime("%d/%m/%Y"),
                "itens": itens_para_tela,
                "valor_total": venda.valor_total()
            })

    def pega_venda_por_id(self, id: int):
        for venda in self.__vendas:
            if venda.id == id:
                return venda
        return None

    def alterar_venda(self):
        self.listar_vendas()
        id_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_por_id(id_venda)

        if venda:
            self.__tela_venda.mostra_mensagem("Selecione o novo cliente e farmacêutico para a venda.")
            
            try:
                self.__controlador_sistema.controlador_cliente.lista_clientes()
                novo_cpf_cliente = self.__tela_venda.pega_cpf_cliente()
                if not novo_cpf_cliente:
                    self.__tela_venda.mostra_mensagem("CPF do novo cliente não fornecido. Cliente não alterado.")
                    return
                
                novo_cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(novo_cpf_cliente)
                if not novo_cliente:
                    raise ClienteNaoEncontrado("Novo cliente não encontrado.")
                
                venda.cliente = novo_cliente
                self.__tela_venda.mostra_mensagem("Cliente da venda atualizado.")

                self.__controlador_sistema.controlador_farmaceutico.lista_farmaceuticos()
                novo_cpf_farmaceutico = self.__tela_venda.pega_cpf_farmaceutico()
                if not novo_cpf_farmaceutico:
                    self.__tela_venda.mostra_mensagem("CPF do novo farmacêutico não fornecido. Farmacêutico não alterado.")
                    return

                novo_farmaceutico = self.__controlador_sistema.controlador_farmaceutico.pega_farmaceutico_por_cpf(novo_cpf_farmaceutico)
                if not novo_farmaceutico:
                    raise FarmaceuticoNaoEncontrado("Novo farmacêutico não encontrado.")
                
                venda.farmaceutico = novo_farmaceutico
                self.__tela_venda.mostra_mensagem("Farmacêutico da venda atualizado.")
                self.__tela_venda.mostra_mensagem("Venda alterada com sucesso.")

            except (ClienteNaoEncontrado, FarmaceuticoNaoEncontrado) as e:
                self.__tela_venda.mostra_mensagem(e.args[0])
            except ValueError:
                self.__tela_venda.mostra_mensagem("CPF inválido.")
            except Exception as e:
                self.__tela_venda.mostra_mensagem(f"Erro inesperado na alteração: {e}.")

        else:
            self.__tela_venda.mostra_mensagem("Venda não encontrada.")

    def excluir_venda(self):
        self.listar_vendas()
        id_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_por_id(id_venda)

        if venda:
            self.__vendas.remove(venda)
            self.__tela_venda.mostra_mensagem("Venda excluída com sucesso.")
        else:
            self.__tela_venda.mostra_mensagem("Venda não encontrada.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def get_vendas(self):
        return self.__vendas
    
    def get_vendas_por_periodo(self, data_inicio: date, data_fim: date) -> list[Venda]:
        vendas_filtradas = [
            venda for venda in self.__vendas if data_inicio <= venda.data <= data_fim
        ]
        return vendas_filtradas

    def abre_tela(self):
        opcoes = {
            1: self.registrar_venda,
            2: self.alterar_venda,
            3: self.listar_vendas,
            4: self.excluir_venda,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_venda.tela_opcoes()
            if opcao == -1:
                continue
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
            elif opcao == 0:
                break
            else:
                self.__tela_venda.mostra_mensagem("Opção inválida. Por favor, escolha uma das opções acima.")