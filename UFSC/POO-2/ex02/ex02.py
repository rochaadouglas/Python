class Pessoa:
    
    def __init__(self, nome = ""):
        self.__nome = nome
        
    
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
uma_pessoa = Pessoa("Jean")
uma_pessoa.nome = "Douglas"
print(uma_pessoa.nome)

outra_pessoa = Pessoa("Paulo")
outra_pessoa.nome = "Outro Nome"
print(outra_pessoa.nome)

uma_pessoa2 = Pessoa("Jean")
print(uma_pessoa2.__nome)