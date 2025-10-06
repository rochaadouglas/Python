from transporte import Transporte

class TrechoRota:
    
    def __init__(self, id_trecho_rota: int, data: str, local_origem: str, local_destino: str, tipo_transporte: Transporte):
        self.__id_trecho_rota = None
        self.__data = None
        self.__local_origem = None
        self.__local_destino = None
        self.__tipo_transporte = None
        
        if isinstance(id_trecho_rota, int):
            self.__id_trecho_rota = id_trecho_rota
        if isinstance(data, str):
            self.__data = data
        if isinstance(local_origem, str):
            self.__local_origem = local_origem
        if isinstance(local_destino, str):
            self.__local_destino = local_destino
        if isinstance(tipo_transporte, Transporte):
            self.__tipo_transporte = tipo_transporte
            
    
    @property
    def id_trecho_rota(self):
        return self.__id_trecho_rota
    
    @id_trecho_rota.setter
    def id_trecho_rota(self, id_trecho_rota: int):
        if isinstance(id_trecho_rota, int):
            self.__id_trecho_rota = id_trecho_rota
            
            
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: str):
        if isinstance(data, str):
            self.__data = data
            
            
    @property
    def local_origem(self):
        return self.__local_origem
    
    @local_origem.setter
    def local_origem(self, local_origem: str):
        if isinstance(local_origem, str):
            self.__local_origem = local_origem
            
    
    @property
    def local_destino(self):
        return self.__local_destino
    
    @local_destino.setter
    def local_destino(self, local_destino: str):
        if isinstance(local_destino, str):
            self.__local_destino = local_destino
            
            
    @property
    def tipo_transporte(self):
        return self.__tipo_transporte
    
    @tipo_transporte.setter
    def tipo_transporte(self, tipo_transporte: Transporte):
        if isinstance(tipo_transporte, Transporte):
            self.__tipo_transporte = tipo_transporte