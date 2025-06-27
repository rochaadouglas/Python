from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        # Nao esqueca de garantir que o objeto recebido pertence a classe Livro...
        # Nao permitir insercao de Livros duplicados!
        if livro is None:
            print("Livro inválido.")
            return
        if not isinstance(livro, Livro):
            print("O objeto não pertence a classe Livro.")
            return
        if livro in self.__livros:
            print("Livro está na biblioteca.")
            return
        self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        if livro in self.__livros:
            self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros