

class PedidoDuplicadoException(Exception):
    
    def __init__(self, meu_pedido):
        super().__init__(f"Pedido com número {meu_pedido} já existe.")