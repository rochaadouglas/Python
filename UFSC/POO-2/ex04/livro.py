class Livro:

    def __init__(self, codigo: int, titulo: str, ano: int, editora, autor, numero_capitulo: int, titulo_cap: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano