

from autor import Autor
from editora import Editora
from capitulo import Capitulo

class Livro:

    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_cap: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo, str):    
            self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if isinstance(ano, int):
            self.__ano = ano

    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora

    def autores(self, autor = []):
        self.autores = autor