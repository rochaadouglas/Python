from abstractTipoChamado import AbstractTipoChamado


class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(nome, str):
            self.__nome = nome
            
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def nome(self):
        return self.__nome