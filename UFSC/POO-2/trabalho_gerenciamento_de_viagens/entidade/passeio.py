class Passeio: 
    
    def __init__(self, id_passeio: int, ponto_turistico: str, horario_inicio: str, horario_fim: str, valor: str):
        self.__id_passeio = None
        self.__ponto_turistico = None
        self.__horario_inicio = None
        self.__horario_fim = None
        self.__valor = None
        
        if isinstance(id_passeio, int):
            self.__id_passeio = id_passeio
        if isinstance(ponto_turistico, str):
            self.__ponto_turistico = ponto_turistico
        if isinstance(horario_inicio, str):
            self.__horario_inicio = horario_inicio
        if isinstance(horario_fim, str):
            self.__horario_fim = horario_fim
        if isinstance(valor, str):
            self.__valor = valor
        
    @property
    def id_passeio(self):
        return self.__id_passeio
    
    @id_passeio.setter
    def id_passeio(self, id_passeio: int):
        if isinstance(id_passeio, int):
            self.__id_passeio = id_passeio
            
            
    @property
    def ponto_turistico(self):
        return self.__ponto_turistico
    
    @ponto_turistico.setter
    def ponto_turistico(self, ponto_turistico: str):
        if isinstance(ponto_turistico, str):
            self.__ponto_turistico = ponto_turistico
            
            
    @property
    def horario_inicio(self):
        return self.__horario_inicio
    
    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: str):
        if isinstance(horario_inicio, str):
            self.__horario_inicio = horario_inicio
            
            
    @property
    def horario_fim(self):
        return self.__horario_fim
    
    @horario_fim.setter
    def horario_fim(self, horario_fim: str):
        if isinstance(horario_fim, str):
            self.__horario_fim = horario_fim
            
            
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor: str):
        if isinstance(valor, str):
            self.__valor = valor