from cliente_fidelidade import ClienteFidelidade
from tipo_pedido import TipoPedido
from pedido import Pedido
from controlador_pedidos import ControladorPedidos

#criar um cliente fidelidade
cliente_fid = ClienteFidelidade(1, 0.2, "00099939393", "Ouglas", "Rua dos s", "99999999")

#criar um tipo de pedido
tipo_pedido = TipoPedido("perecivel", 2.0)

#criar um pedido
pedido1 = Pedido(1, cliente_fid, tipo_pedido)

#incluir itens
pedido1.inclui_item_pedido(1, "abacate", 5.0)
pedido1.inclui_item_pedido(2, "banana", 3.0)

#mostrar itens
print("Itens do pedido")
for item in pedido1.itens:
    print(f"{item.descricao}: {item.preco_unitario}")