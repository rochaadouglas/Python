from passeio import Passeio

class Local:
    
    def __init__(self, id_local: int, cidade: str, pais: str, passeio: Passeio):
        self.__id_local = None
        self.__cidade = None
        self.__pais = None
        self.__passeio = None
        
        if isinstance(id_local, int):
            self.__id_local = id_local
        if isinstance(cidade, str):
            self.__cidade = cidade
        if isinstance(pais, str):
            self.__pais = pais
        if isinstance(passeio, Passeio):
            self.__passeio = passeio
            
        
    @property
    def id_local(self):
        return self.__id_local
    
    @id_local.setter
    def id_local(self, id_local: int):
        if isinstance(id_local, int):
            self.__id_local = id_local
            
            
    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade: str):
        if isinstance(cidade, str):
            self.__cidade = cidade
            
            
    @property
    def pais(self):
        return self.__pais
    
    @pais.setter
    def pais(self, pais: str):
        if isinstance(pais, str):
            self.__pais = pais
            
            
    @property
    def passeio(self):
        return self.__passeio
    
    @passeio.setter
    def passeio(self, passeio: Passeio):
        if isinstance(passeio, Passeio):
            self.__passeio = passeio