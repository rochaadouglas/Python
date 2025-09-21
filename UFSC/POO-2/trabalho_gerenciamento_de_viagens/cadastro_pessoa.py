class CadastroPessoa:
    
    def __init__(self, nome: str, celular: str, informacao: str):
        self.__nome = None
        self.__celular = None
        self.__informacao = None
        
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(celular, str):
            self.__celular = celular
        if isinstance(informacao, str):
            self.__informacao = informacao
            
            
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
    def informacao(self):
        return self.__informacao
    
    @informacao.setter
    def informacao(self, informacao: str):
        if isinstance(informacao, str):
            self.__informacao = informacao