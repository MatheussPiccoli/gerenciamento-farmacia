from cliente import Cliente
from farmaceutico import Farmaceutico
from medicamento import Medicamento
from itemvenda import ItemVenda
from lote import LoteMedicamento
from estoque import Estoque
from venda import Venda
from pessoa import Pessoa

c1 = Cliente("João", "123456789", 23 , 987654321)
f1 = Farmaceutico("Maria", "13246578", 20 , 3000)
m1 = Medicamento("Paracetamol", "Generico", 10.0 )
item1 = ItemVenda(m1, 2)
m2 = Medicamento("Ibuprofeno", "Generico", 15.0 )
item2 = ItemVenda(m2, 1)
venda1 = Venda(c1, f1, "2023-10-01")
estoque = Estoque()
lote1 = LoteMedicamento(m1, "Lote123", "2024-12-31", 100)
lote2 = LoteMedicamento(m2, "Lote456", "2025-06-30", 50)
estoque.add_lote(lote1)
estoque.add_lote(lote2)
print(estoque.consultar_estoque(m1))
estoque.baixar_estoque(m1, 2)
print(estoque.consultar_estoque(m1))
venda1.adicionar_item(item1)
venda1.adicionar_item(item2)
venda1.remover_item(item2)
f1.registrar_venda(venda1)
print(f"Venda registrada: {venda1.cliente.nome} comprou {len(venda1.itens)} itens com o farmacêutico {venda1.farmaceutico.nome} na data {venda1.data} com o total de RS{venda1.valor_total()}")