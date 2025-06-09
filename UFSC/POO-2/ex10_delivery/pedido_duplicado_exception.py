

class PedidoDuplicadoException(Exception):
    def __init__(self, numero_pedido):
        super().__init__(f"Pedido com número {numero_pedido} já existe.")