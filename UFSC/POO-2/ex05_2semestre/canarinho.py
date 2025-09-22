from ave import Ave

class Canarinho(Ave):
    
    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo=100, altura_voo=150)
    
    def produzir_som(self):
        return f"AVE: PRODUZ SOM: PIU"
        
    def cantar(self):
        return self.produzir_som()