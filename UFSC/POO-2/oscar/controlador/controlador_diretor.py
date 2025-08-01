from entidade.diretor import Diretor
from limite.tela_diretor import TelaDiretor
from exception.diretor_repetido_exception import DiretorRepetidoException

class ControladorDiretor():
    
    def __init__(self, controlador_sistema):
        self.__diretores = []
        self.__tela_diretor = TelaDiretor()
        self.__controlador_sistema = controlador_sistema
        
    def pega_diretor(self, id: int):
        for diretor in self.__diretores:
            if diretor.id == id:
                return diretor
        return None
    
    def lista_diretores(self):
        for diretor in self.__diretores:
            self.__tela_diretor.mostra_diretor({"id": diretor.id, "nome": diretor.nome,
                                                "data_de_nascimento": diretor.data_de_nascimento, 
                                                "nacionalidade": diretor.nacionalidade})   
    
    def alterar_diretor(self):
        self.lista_diretores()
        id_diretor = self.__tela_diretor.seleciona_diretor()
        diretor = self.pega_diretor(id_diretor)
        
        if(diretor is not None):
            novos_dados_diretor = self.__tela_diretor.pega_dados_diretor()
            diretor.id = novos_dados_diretor["id"]
            diretor.nome = novos_dados_diretor["nome"]
            diretor.data_de_nascimento = novos_dados_diretor["data_de_nascimento"]
            diretor.nacinalidade = novos_dados_diretor["nacionalidade"]
            self.lista_atores()
        else:
            self.__tela_diretor.mostra_mensagem("Este diretor não existe.")
    
    def incluir_diretor(self):
        dados_diretor = self.__tela_diretor.pega_dados_diretor()
        id = dados_diretor["id"]
        diretor = self.pega_diretor(id)
        try: 
            if diretor == None:
                diretor = Diretor(dados_diretor["id"], dados_diretor["nome"],
                              dados_diretor["data_de_nascimento"], dados_diretor["nacionalidade"])
                self.__diretores.append(diretor)
            else:
                raise DiretorRepetidoException(id)
        except DiretorRepetidoException as e:
            self.__tela_diretor.mostra_mensagem(e)
            
    def excluir_diretor(self):
        self.lista_diretores()
        id_diretor = self.__tela_diretor.seleciona_diretor()
        diretor = self.pega_diretor(id_diretor)
        
        if diretor is not None:
            self.__diretores.remove(diretor)
            self.lista_diretores()
        else:
            self.__tela_diretor.mostra_mensagem("Este diretor não existe.")
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()
            
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_diretor, 2: self.alterar_diretor,
                        3: self.lista_diretores, 4: self.excluir_diretor, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_diretor.tela_opcoes()]()