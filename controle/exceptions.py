class DadoInvalidoException(Exception):
    def __init__(self):
        super().__init__("Dado(s) inválido(s)")

class MedicamentoNaoEncontrado(Exception):
    def __init__(self):
        super().__init__("Medicamento não encontrado no estoque")

class VendaNaoExistente(Exception):
    def __init__(self):
        super().__init__("Venda não encontrada")

class FarmaceuticoNaoExistente(Exception):
    def __init__(self):
        super().__init__("Farmaceutico não encontrado")

class EstoqueVazio(Exception):
    def __init__(self):
        super().__init__("Estoque vazio")
    
class EstoqueInsuficiente(Exception):
    def __init__(self):
        super().__init__("Estoque insuficiente")

class ClienteNaoEncontrado(Exception):
    def __init__(self, message="Cliente não encontrado"): 
        super().__init__(message) 

class FarmaceuticoNaoEncontrado(Exception):
    pass