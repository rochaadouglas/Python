from entidade.ator import Ator
from limite.tela_ator import TelaAtor

class ControladorAtor():
    
    def __init__(self, controlador_sistema):
        self.__atores = []
        self.__tela_ator = TelaAtor()
    
    def incluir_ator(self):
        pass