class Ordenacao():

    def ordena(self, array_para_ordenar = []): #Realiza a ordenacao do conteudo do array recebido como parâmetro
        self.ordenar = array_para_ordenar
        self.nova_lista = []
        for i in self.ordenar:
            if i <= 2:
                self.nova_lista = i        
        return self.nova_lista

    def to_string(self, array_ordenado = []):
        return
    
lista = [2, 3, 5, 1, 5]
ord = Ordenacao()
print(ord.ordena(lista))