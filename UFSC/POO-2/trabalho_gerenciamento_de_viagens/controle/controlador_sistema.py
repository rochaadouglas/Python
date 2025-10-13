from tela.tela_sistema import TelaSistema
from controle.controlador_pessoa import ControladorPessoa
from tela.tela_pessoa import TelaPessoa

class ControladorSistema:
    
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__tela_pessoa = TelaPessoa()
    
    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa
    
    def inicializa_sistema(self):
        self.abre_tela()
        
    def abre_tela(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            
            if opcao == 1:
                self.__controlador_pessoa.abre_tela()
            elif opcao == 0:
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")