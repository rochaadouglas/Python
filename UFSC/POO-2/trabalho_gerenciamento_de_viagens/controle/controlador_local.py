from entidade.local import Local
from tela.tela_local import TelaLocal


class ControladorLocal:
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__locais = []
        self.__tela_local = TelaLocal()
        
    #agora os métodos
    
    def abre_tela(self):
        pass