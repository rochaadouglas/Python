

from autor import Autor
from editora import Editora
from capitulo import Capitulo

class Livro:

    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_cap: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = []
        self.__capitulos = []

        if isinstance(autor, Autor):
            self.__autores.append(autor)
        
        if isinstance(numero_capitulo, int) and isinstance(titulo_cap, str):
            capitulo = Capitulo(numero_capitulo, titulo_cap)
            self.__capitulos.append(capitulo)
            #self.__capitulos.append(Capitulo(numero_capitulo, titulo_cap))

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

    @property
    def autores(self):
        return self.__autores
    
    def incluir_autor(self, autor):
        if isinstance(autor, Autor):
            if autor not in self.__autores:
                self.__autores.append(autor)

    def excluir_autor(self, autor):
        if autor in self.__autores:
            self.__autores.remove(autor)

    def incluir_capitulo(self, numero, titulo):
        if isinstance(numero, int) and isinstance(titulo, str):
            for i in self.__capitulos:
                if i.titulo == titulo:
                    break
            else:
                cap = Capitulo(numero, titulo)
                self.__capitulos.append(cap)

    def find_capitulo_by_titulo(self, titulo):
        for i in self.__capitulos:
            if i.titulo == titulo:
                return i