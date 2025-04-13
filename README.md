```
UNIVERSIDADE FEDERAL DE SANTA CATARINA
Disciplina: INE5605 – Desenvolvimento de Sistemas Orientados a Objetos I
Professores: Thaís Idalino, Douglas Hiura Longo e André Bräscher
```
# Trabalho 1

## PROBLEMA:

Desenvolver um sistema orientado a objetos em Python para gerenciamento de uma
farmácia, permitindo a administração de medicações, e o rastreio de compras e vendas
de clientes e farmacêuticos.

## ESCOPO DO DESENVOLVIMENTO:

O sistema da farmácia deve permitir o cadastro e gerenciamento de medicamentos,
clientes, farmacêuticos e transações de compra e venda. Ele deverá garantir a
rastreabilidade dos produtos comercializados, mantendo um histórico organizado e
preciso das operações realizadas.
O cadastro de medicamentos deve conter: nome, fabricante, data de validade,
quantidade em estoque e preço unitário.
Cada transação deve registrar a data, o responsável (cliente e farmacêutico), os itens
vendidos (medicamentos), a quantidade e o valor total da operação.


## REGRAS DO SISTEMA:

1. Apenas farmacêuticos cadastrados podem registrar uma venda.
2. Cada venda deve associar o cliente e o farmacêutico responsáveis.
3. O sistema deve impedir a venda de medicamentos com estoque insuficiente ou
vencidos.
4. O sistema deve permitir o cadastro, edição, remoção e listagem de medicamentos,
clientes e farmacêuticos.
5. Cada transação de venda deve ser registrada e ficar disponível para consulta
posterior.

## RESTRIÇÕES DE ESCOPO:

Para simplificar este trabalho, o sistema contemplará apenas funcionalidades básicas de
uma farmácia, sem considerar integrações com sistemas fiscais ou prescrições médicas.
O sistema deve considerar:
● **Cadastros:** inclusão, exclusão, alteração e listagem de clientes, farmacêuticos e
medicamentos.
○ Clientes (ID, nome, CPF, telefone);
○ Farmacêuticos (ID, nome, CRF, telefone);
○ Medicamentos (nome, fabricante, validade, preço e quantidade).
● **Registros:** inclusão, exclusão, alteração e listagem de transações de
vendas.
● **Relatórios:**


○ Listar medicamentos em estoque com filtro por validade ou fabricante;
○ Listar vendas por período, cliente ou farmacêutico;
○ Relatório de medicamentos mais vendidos;
○ Listar clientes que mais compraram no mês;
○ Relatório de medicamentos vencidos ou com estoque baixo.


