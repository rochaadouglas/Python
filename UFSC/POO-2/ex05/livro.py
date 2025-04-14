from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        # Criar todos os atributos, incluindo as listas
        # Incluir o primeiro autor e o primeiro capitulo nas respectivas listas
        self.__codigo = None
        self.__titulo = None
        self.__ano = None
        self.__editora = None
        self.__autores = []
        self.__capitulos = []
        um_capitulo = Capitulo(numero_capitulo, titulo_capitulo)
        self.__capitulos.append(um_capitulo)
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(ano, int):
            self.__ano = ano
        if isinstance(editora, Editora):
            self.__editora = editora
        if isinstance(autor, Autor):
            self.__autores.append(autor)
        

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo


    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
    
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano: int):
        if isinstance(ano, int):                                    
            self.__ano = ano
            
    
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, editora: Editora):
        if isinstance(editora, Editora):
            self.__editora = editora
    
    
    def incluir_autor(self, autor: Autor):
        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        # Nao permitir insercao de Autores duplicados!
        if isinstance(autor, Autor):
            self.__autor.append(autor)

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str):
        um_capitulo = Capitulo(numero, titulo)
        self.__capitulos.append(um_capitulo)

    def excluir_capitulo(self, titulo: str):
        capitulo = self.find_capitulo_by_titulo(titulo)
        self.__capitulos.remove(capitulo)
        
    def find_capitulo_by_titulo(self, titulo: str):
        # Procura na lista de capitulos se existe um Capitulo com este titulo 
        # Se encontrar, retorna o Capitulo encontrado
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo