from pessoa import Pessoa
from trecho_rota import TrechoRota
from local import Local

class PacoteViagem:
    
    def __init__(self, id_viagem: int, comprador: Pessoa, grupo: Pessoa, data_inicio: str, data_fim: str,
                 local: Local, trecho_rota: TrechoRota):
        self.__id_viagem = None
        self.__comprador = None
        self.__grupo = None
        self.__data_inicio = None
        self.__data_fim = None
        self.__local = None
        self.__trecho_rota = None
        
        if isinstance(id_viagem, int):
            self.__id_viagem = id_viagem
        if isinstance(comprador, Pessoa):
            self.__comprador = comprador
        if isinstance(grupo, Pessoa):
            self.__grupo = []
        if isinstance(data_inicio, str):
            self.__data_inicio = data_inicio
        if isinstance(data_fim, str):
            self.__data_fim = data_fim
        if isinstance(local, Local):
            self.__local = local
        if isinstance(trecho_rota, TrechoRota):
            self.__trecho_rota = []
            
            
    @property
    def id_viagem(self):
        return self.__id_viagem
    
    @id_viagem.setter
    def id_viagem(self, id_viagem: int):
        if isinstance(id_viagem, int):
            self.__id_viagem = id_viagem
            
            
    @property
    def comprador(self):
        return self.__comprador
    
    @comprador.setter
    def comprador(self, comprador: Pessoa):
        if isinstance(comprador, Pessoa):
            self.__comprador = comprador
            
    
    @property
    def grupo(self):
        return self.__grupo
    
    @grupo.setter
    def grupo(self, grupo: Pessoa):
        if isinstance(grupo, Pessoa):
            self.__grupo = []
            
            
    @property
    def data_inicio(self):
        return self.__data_inicio
    
    @data_inicio.setter
    def data_inicio(self, data_inicio: str):
        if isinstance(data_inicio, str):
            self.__data_inicio = data_inicio
            
            
    @property
    def data_fim(self):
        return self.__data_fim
    
    @data_fim.setter
    def data_fim(self, data_fim: str):
        if isinstance(data_fim, str):
            self.__data_fim = data_fim
            
            
    @property
    def local(self):
        return self.__local
    
    @local.setter
    def local(self, local: Local):
        if isinstance(local, Local):
            self.__local = local
            
            
    @property
    def trecho_rota(self):
        return self.__trecho_rota
    
    @trecho_rota.setter
    def trecho_rota(self, trecho_rota: TrechoRota):
        if isinstance(trecho_rota, TrechoRota):
            self.__trecho_rota = []