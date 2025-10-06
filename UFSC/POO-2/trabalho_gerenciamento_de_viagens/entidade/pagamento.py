class Pagamento:
    
    def __init__(self, id_pagamento: int, data: str, valor_pago: str):
        self.__id_pagamento = None
        self.__data = None
        self.__valor_pago = None
        
        if isinstance(id_pagamento, int):
            self.__id_pagamento = id_pagamento
        if isinstance(data, str):
            self.__data = data
        if isinstance(valor_pago, str):
            self.__valor_pago = valor_pago
            
            
    @property
    def id_pagamento(self):
        return self.__id_pagamento
    
    @id_pagamento.setter
    def id_pagamento(self, id_pagamento: int):
        if isinstance(id_pagamento, int):
            self.__id_pagamento = id_pagamento
            
            
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: str):
        if isinstance(data, str):
            self.__data = data
            
            
    @property
    def valor_pago(self):
        return self.__valor_pago
    
    @valor_pago.setter
    def valor_pago(self, valor_pago: str):
        if isinstance(valor_pago, str):
            self.__valor_pago = valor_pago