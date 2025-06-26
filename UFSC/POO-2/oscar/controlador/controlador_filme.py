from entidade.filme import Filme
from limite.tela_filme import TelaFilme
from exception.filme_repetido_exception import FilmeRepetidoException

class ControladorFilme():
    
    def __init__(self, controlador_sistema):
        self.__filmes = []
        self.__tela_filme = TelaFilme()
        self.__controlador_sistema = controlador_sistema