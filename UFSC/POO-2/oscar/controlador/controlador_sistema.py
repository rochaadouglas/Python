from limite.tela_sistema import TelaSistema
from controlador.controlador_ator import ControladorAtor
from controlador.controlador_categoria import ControladorCategoria
from controlador.controlador_diretor import ControladorDiretor

class ControladorSistema:
    
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_ator = ControladorAtor(self)
        self.__controlador_categoria = ControladorCategoria(self)
        self.__controlador_diretor = ControladorDiretor(self)
        
    @property
    def controlador_ator(self):
        return self.__controlador_ator
    
    @property
    def controlador_categoria(self):
        return self.__controlador_categoria
    
    @property
    def controlador_diretor(self):
        return self.__controlador_diretor
    
    #metodo que inializa o sistema, chamando o metodo abre_tela.   
    def inicializa_sistema(self):
        self.abre_tela()
    
    
    #metodo que mostram as opções da tela inicial, e onde tudo começa.    
    def abre_tela(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            
            if opcao == 1:
                self.__controlador_ator.abre_tela()
            elif opcao == 2:
                self.__controlador_categoria.abre_tela()
            elif opcao == 3:
                self.__controlador_diretor.abre_tela()
                break
            else:
                self.__tela_sistema.mostra_mensagem("Opção inválida.")
                
    def pega_ator(self, id: int):
        return self.__controlador_ator.pega_ator(id)