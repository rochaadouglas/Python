class Transporte:
    
    def __init__(self, id_transporte: str, tipo: str):
        self.__id_transporte = None
        self.__tipo = None
        
        if isinstance(id_transporte, int):
            self.__id_transporte = id_transporte
        if isinstance(tipo, str):
            self.__tipo = tipo
            
        
    @property
    def id_transporte(self):
        return self.__id_transporte
    
    @id_transporte.setter
    def id_transporte(self, id_transporte: int):
        if isinstance(id_transporte, int):
            self.__id_transporte = id_transporte
            
            
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo