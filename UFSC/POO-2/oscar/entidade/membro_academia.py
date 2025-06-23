from abc import ABC
from entidade.votavel import Votavel

class MembroAcademia(Votavel, ABC):
    
    def __init__(self, id: int, nome: str, 
                 data_de_nascimento: str, nacionalidade: str):
        super().__init__(id)
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(data_de_nascimento, str):
            self.__data_de_nascimento = data_de_nascimento
        if isinstance(nacionalidade, str):
            self.__nacionalidade = nacionalidade
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
            
            
    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento
    
    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento: str):
        if isinstance(data_de_nascimento, str):
            self.__data_de_nascimento = data_de_nascimento
            
            
    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nacionalidade: str):
        if isinstance(nacionalidade, str):
            self.__nacionalidade = nacionalidade