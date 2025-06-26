from entidade.filme import Filme
from limite.tela_filme import TelaFilme
from exception.filme_repetido_exception import FilmeRepetidoException

class ControladorFilme():
    
    def __init__(self, controlador_sistema):
        self.__filmes = []
        self.__tela_filme = TelaFilme()
        self.__controlador_sistema = controlador_sistema
        
    def pega_filme(self, id: int):
        for filme in self.__filmes:
            if filme.id == id:
                return filme
            
    def incluir_filme(self):
        dados_filme = self.__tela_filme.pega_dados_filme()
        id = dados_filme["id"]
        filme = self.pega_filme(id)
        try: 
            if filme == None:
                filme = Filme(dados_filme["id"], dados_filme["titulo"], 
                              dados_filme["nome_diretor"], dados_filme["ano"])
                self.__filmes.append(filme)
            else:
                raise FilmeRepetidoException(id)
        except FilmeRepetidoException as e:
            self.__tela_filme.mostra_mensagem(e)
    
    def lista_filmes(self):
        for filme in self.__filmes:
            self.__tela_filme.mostra_filme({"id": filme.id, "titulo": filme.titulo,
                                             "nome_diretor": filme.nome_diretor, "ano": filme.ano})
            
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_filme,
                        3: self.lista_filmes}
        continua = True
        while continua:
            lista_opcoes[self.__tela_filme.tela_opcoes()]()