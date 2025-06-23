from entidade.diretor import Diretor

class Filme:
    
    def __init__(self, titulo: str, diretor: Diretor, ano: int):
        self.__categorias = []
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(diretor, Diretor):
            self.__diretor = diretor
        if isinstance(ano, int):
            self.__ano = ano