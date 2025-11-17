from entidade.pessoa import Pessoa
from tela.tela_pessoa import TelaPessoa
from exception.pessoa_repetida_exception import PessoaRepetidaException

class ControladorPessoa:
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pessoas = []
        self.__tela_pessoa = TelaPessoa()
        
    def pega_pessoa(self, id):
        for pessoa in self.__pessoas:
            if pessoa.identificacao == id:
                return pessoa
        return None
    
    def incluir_pessoa(self):
        dados = self.__tela_pessoa.pega_dados_pessoa()
        id = dados["identificacao"]
        pessoa = self.pega_pessoa(id)
        try:
            if pessoa == None:
                pessoa = Pessoa(dados["nome"], dados["celular"], dados["identificacao"])
                self.__pessoas.append(pessoa)
            else:
                raise PessoaRepetidaException(id)
        except PessoaRepetidaException as e:
            self.__tela_pessoa.mostra_pessoa(e)
                              
    def listar_pessoa(self):
        for pessoa in self.__pessoas:
            self.__tela_pessoa.mostra_pessoa({"nome": pessoa.nome, "celular": pessoa.celular,
                                              "identificacao": pessoa.identificacao})
                        
    def excluir_pessoa(self):
        identificacao = self.__tela_pessoa.pega_identificacao()
        pessoa = self.busca_pessoa_por_id(identificacao)
        if pessoa:
            self.__pessoas.remove(pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa removida com sucesso.")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
        
    def busca_pessoa_por_id(self, identificacao: str):
        for pessoa in self.__pessoas:
            if pessoa.identificacao == identificacao:
                return pessoa
        return None
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_pessoa, 2: self.listar_pessoa,
                        3: self.excluir_pessoa, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()