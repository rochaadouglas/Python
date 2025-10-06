from pagamento import Pagamento

class Pix(Pagamento):
    
    def __init__(self, id_pagamento, data, valor_pago):
        super().__init__(id_pagamento, data, valor_pago)