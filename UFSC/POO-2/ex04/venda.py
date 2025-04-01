from cliente import Cliente
from pacote_viagem import PacoteViagem

class Venda:

    def __init__(self, codigo: int, cliente: Cliente, descricao: str, pacote: PacoteViagem, quantidade: int):
        self.__codigo = None
        self.__cliente = None
        self.__descricao = None
        self.__pacote = None
        self.__quantidade = None
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(pacote, PacoteViagem):
            self.__pacote = pacote
        if isinstance(quantidade, int):
            self.__quantidade = quantidade


    @property
    def codigo(self):
        return self.__codigo
        
    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
                
                
    @property
    def cliente(self):
        return self.__cliente
        
    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        
        
    @property
    def descricao(self):
        return self.__descricao
        
    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
                
        
    @property
    def pacote(self):
        return self.__pacote
        
    @pacote.setter
    def pacote(self, pacote: PacoteViagem):
        if isinstance(pacote, PacoteViagem):
            self.__pacote = pacote
        
        
    @property
    def quantidade(self):
        return self.__quantidade
        
    @quantidade.setter
    def quantidade(self, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
        
    
    def preco_total(self):
        return self.__quantidade * self.__pacote.custo_unitario


cliente01 = Cliente("Douglas", 88991234, "doug.r@htm.com")
pact = PacoteViagem("São José", "Floripa", 5, 50.99)
venda01 = Venda(333, cliente01, "dinheiro", pact, 2)
print(venda01.preco_total())