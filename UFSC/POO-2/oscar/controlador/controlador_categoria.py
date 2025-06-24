from limite.tela_categoria import TelaCategoria
from entidade.categoria import Categoria
from exception.categoria_repetida_exception import CategoriaRepetidaException

class ControladorCategoria():
    
    def __init__(self, controlador_sistema):
        self.__categorias = []
        self.__tela_categoria = TelaCategoria()
        self.__controlador_sistema = controlador_sistema
        
    def pega_categoria(self, nome: str):
        for categoria in self.__categorias:
            if categoria.nome == nome:
                return categoria
        return None
    
    def incluir_categoria(self):
        dados_categoria = self.__tela_categoria.pega_dados_categoria()
        nome = dados_categoria["nome"]
        categoria = self.pega_categoria(nome)
        try:
            if categoria == None:
                categoria = Categoria(dados_categoria["nome"])
                self.__categorias.append(categoria)
            else:
                raise CategoriaRepetidaException(nome)
        except CategoriaRepetidaException as e:
            self.__tela_categoria.mostra_mensagem(e)
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_categoria}
        continua = True
        while continua:
            lista_opcoes[self.__tela_categoria.tela_opcoes()]()