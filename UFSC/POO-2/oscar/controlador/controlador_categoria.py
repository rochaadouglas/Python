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
    
    def lista_categorias(self):
        for categoria in self.__categorias:
            self.__tela_categoria.mostra_categoria({"nome": categoria.nome})
    
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
            
    def alterar_categoria(self):
        self.lista_categorias()
        nome_categoria = self.__tela_categoria.seleciona_categoria()
        categoria = self.pega_categoria(nome_categoria)
        
        if(categoria is not None):
            novo_nome_categoria = self.__tela_categoria.pega_dados_categoria()
            categoria.nome = novo_nome_categoria["nome"]
            self.lista_categorias()
        else:
            self.__tela_categoria.mostra_mensagem("Esta categoria não existe.")
    
    def excluir_categoria(self):
        self.lista_categorias()
        nome_categoria = self.__tela_categoria.seleciona_categoria()
        categoria = self.pega_categoria(nome_categoria)
        
        if categoria is not None:
            self.__categorias.remove(categoria)
            self.lista_categorias()
        else:
            self.__tela_categoria.mostra_mensagem("Esta categoria não existe.")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_categoria, 2: self.alterar_categoria,
                        3: self.lista_categorias, 4: self.excluir_categoria, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_categoria.tela_opcoes()]()