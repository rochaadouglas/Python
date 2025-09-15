

class Produto:
    
    def __init__(self, codigo = int, descricao = str, categoria_produto = str, quantidade = int, preco_unitario = float, cliente = str):
        self.__codigo = None
        self.__descricao = None
        self.__categoria_produto = None
        self.__quantidade = None
        self.__preco_unitario = None
        self.__cliente = None
        
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(categoria_produto, str):
            self.__categoria_produto = categoria_produto
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
        if isinstance(preco_unitario, int):
            self.__preco_unitario = preco_unitario
        if isinstance(cliente, str):
            self.__cliente = cliente
        
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo = int):
        if isinstance(codigo, int):
            self.__codigo = codigo
            
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao = str):
        if isinstance(descricao, str):
            self.__descricao = descricao
            
    
    @property
    def categoria_produto(self):
        return self.__categoria_produto
    
    @categoria_produto.setter
    def categoria_produto(self, categoria_produto = str):
        if isinstance(categoria_produto, str):
            self.__categoria_produto = categoria_produto
            
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade = int):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
            
    
    @property
    def preco_unitario(self):
        return self.__preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, preco_unitario = float):
        if isinstance(preco_unitario, float):
            self.__preco_unitario = preco_unitario
            
            
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente = str):
        if isinstance(cliente, str):
            self.__cliente = cliente
            
    
    def preco_total(self, quantidade, preco_unitario):
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        total = self.quantidade * self.preco_unitario
        
        return total