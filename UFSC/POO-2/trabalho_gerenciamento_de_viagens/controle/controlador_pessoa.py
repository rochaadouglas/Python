from entidade.pessoa import Pessoa
from tela.tela_pessoa import TelaPessoa

class ControladorPessoa:
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pessoas = []
        self.__tela_pessoa = TelaPessoa()
        
        
    def abre_tela(self):
        while True:
            opcao = self.__tela_pessoa.mostra_opcoes()
            if opcao == 1:
                self.incluir_pessoa()
            elif opcao == 2:
                self.listar_pessoa()
            elif opcao == 3:
                self.excluir_pessoa()
            elif opcao == 0:
                break
            
            
    def incluir_pessoa(self):
        dados = self.__tela_pessoa.pega_dados_pessoa()
        nova_pessoa = Pessoa(dados["nome"], dados["celular"], dados["identificacao"])
        self.__pessoas.append(nova_pessoa)
        self.__tela_pessoa.mostra_mensagem("Pessoa cadastrada com sucesso.")
        
        
    def listar_pessoa(self):
        if not self.__pessoas:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in self.__pessoas:
                self.__tela_pessoa.mostra_pessoa(pessoa) #dados da pessoa como dicionário 
                
                
    def excluir_pessoa(self):
        identificacao = self.__tela_pessoa.pega_identificacao()
        pessoa = self.busca_pessoa_por_id(identificacao)
        if pessoa:
            self.__pessoas.remove(pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa removida com sucesso.")
        else:
            self.__tela_pessoa.mostra_mensagem("Pessoa não encontrada.")
        
        
    def busca_pessoa_por_id(self, identificacao: str):
        for pessoa in self.__pessoas:
            if pessoa.identificacao == identificacao:
                return pessoa
        return None