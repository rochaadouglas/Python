class Autor:
    def __init__(self, codigo: int, nome: str):
        self.__codigo = None
        self.__nome = None
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(nome, str):
            self.nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
            
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome