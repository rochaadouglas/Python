class Pessoa:
    
    def __init__(self, nome: str, celular: str, identificacao: str):
        self.__nome = None
        self.__celular = None
        self.__identificacao = None
        
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(celular, str):
            self.__celular = celular
        if isinstance(identificacao, str):
            self.__identificacao = identificacao
            
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
            
            
    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, celular: str):
        if isinstance(celular, str):
            self.__celular = celular
            
            
    @property
    def identificacao(self):
        return self.__identificacao
    
    @identificacao.setter
    def identificacao(self, identificacao: str):
        if isinstance(identificacao, str):
            self.__identificacao = identificacao