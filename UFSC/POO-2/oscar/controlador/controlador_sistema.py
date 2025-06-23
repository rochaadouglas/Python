from limite.tela_sistema import TelaSistema
from controlador.controlador_ator import ControladorAtor

class ControladorSistema:
    
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_ator = ControladorAtor(self)
        
    @property
    def controlador_ator(self):
        return self.__controlador_ator
    
    #metodo que inializa o sistema, chamando o metodo abre_tela.   
    def inicializa_sistema(self):
        self.abre_tela()
    
    
    #metodo que mostram as opções da tela inicial, e onde tudo começa.    
    def abre_tela(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            
            if opcao == 1:
                self.__controlador_ator.abre_tela()
                
    def pega_ator(self, id: int):
        return self.__controlador_ator.pega_ator(id)