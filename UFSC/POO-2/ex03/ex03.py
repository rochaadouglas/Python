class Aluno:
    
    def __init__(self, nome: str, endereco: str):
        self.__nome = None
        self.__endereco = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(endereco, str):
            self.__endereco = endereco
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
            
            
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco