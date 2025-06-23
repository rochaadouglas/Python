from entidade.ator import Ator
from limite.tela_ator import TelaAtor
from exception.ator_repetido_exception import AtorRepetidoException

class ControladorAtor():
    
    def __init__(self, controlador_sistema):
        self.__atores = []
        self.__tela_ator = TelaAtor()
        self.__controlador_sistema = controlador_sistema
    
    def pega_ator(self, id: int):
        for ator in self.__atores:
            if ator.id == id:
                return ator
        return None
    
    def incluir_ator(self):
        dados_ator = self.__tela_ator.pega_dados_ator()
        id = dados_ator["id"]
        ator = self.pega_ator(id)
        try:
            if ator == None:
                ator = Ator(dados_ator["id"], dados_ator["nome"], 
                            dados_ator["data_de_nascimento"], dados_ator["nacionalidade"])
                self.__atores.append(ator)
            else:
                raise AtorRepetidoException(id)
        except AtorRepetidoException as e:
            self.__tela_ator.mostra_ator(e)
            
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_ator}
        continua = True
        while continua:
            lista_opcoes[self.__tela_ator.tela_opcoes()]()