from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        # Nao esqueca de garantir que o objeto recebido pertence a classe Livro...
        # Nao permitir insercao de Livros duplicados!
        if isinstance(livro, Livro):
            self.__livro.append(livro)

    def excluir_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            self.__livro.remove(livro)

    @property
    def livros(self):
        return self.__livros