from cadastro_pessoa import CadastroPessoa
from periodo import Periodo
from tipo_transporte import TipoTransporte

class CadastroGrupo:
    
    def __init__(self, qtdade_pessoa: int, pessoa: CadastroPessoa, 
                 tipo_transporte: TipoTransporte, periodo: Periodo):
        self.__qtdade_pessoa = None
        self.__pessoa = None
        self.__tipo_transporte = None
        self.__periodo = None
        
        if isinstance(qtdade_pessoa, int):
            self.__qtdade_pessoa = qtdade_pessoa
        if isinstance(pessoa, CadastroPessoa):
            self.__pessoa = pessoa
        if isinstance(tipo_transporte, TipoTransporte):
            self.__tipo_transporte = tipo_transporte
        if isinstance(periodo, Periodo):
            self.__periodo = periodo
            
            
    @property
    def qtdade_pessoa(self):
        return self.__qtdade_pessoa
    
    @qtdade_pessoa.setter
    def qtdade_pessoa(self, qtdade_pessoa: str):
        if isinstance(qtdade_pessoa, str):
            self.__qtdade_pessoa = qtdade_pessoa
            
            
    @property
    def pessoa(self):
        return self.__pessoa
    
    @pessoa.setter
    def pessoa(self, pessoa: CadastroPessoa):
        if isinstance(pessoa, CadastroPessoa):
            self.__pessoa = pessoa
            
            
    @property
    def tipo_transporte(self):
        return self.__tipo_transporte
    
    @tipo_transporte.setter
    def tipo_transporte(self, tipo_transporte: TipoTransporte):
        if isinstance(tipo_transporte, TipoTransporte):
            self.__tipo_transporte = tipo_transporte
            
            
    @property
    def periodo(self):
        return self.__periodo
    
    @periodo.setter
    def periodo(self, periodo: Periodo):
        if isinstance(periodo, Periodo):
            self.__periodo = periodo