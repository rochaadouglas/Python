class Ordenacao():

    def ordena(self, array_para_ordenar = []): #Realiza a ordenacao do conteudo do array recebido como parâmetro
        self.ordenar = array_para_ordenar
        self.nova_lista = []
        while self.ordenar:
            self.menor = min(self.ordenar)
            self.ordenar.remove(self.menor)
            self.nova_lista.append(self.menor)
        return self.nova_lista 

    def to_string(self, lista):
        lista_ordenada = self.ordena(lista)
        return " ".join(map(str, self.nova_lista))
    
lista = [4, 3, 2, 1, 5]
ord = Ordenacao()
print(ord.to_string(lista))