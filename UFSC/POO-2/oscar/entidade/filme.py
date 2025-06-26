from entidade.diretor import Diretor
from entidade.votavel import Votavel

class Filme(Votavel):
    
    def __init__(self, titulo: str, diretor: Diretor, ano: int):
        super().__init__(id)
        self.__categorias = []
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(diretor, Diretor):
            self.__diretor = diretor
        if isinstance(ano, int):
            self.__ano = ano
            
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
          
            
    @property
    def diretor(self):
        return self.__diretor
    
    @diretor.setter
    def diretor(self, diretor: str):
        if isinstance(diretor, str):
            self.__diretor = diretor
            
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if isinstance(ano, int):
            self.__ano = ano