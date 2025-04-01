

class PacoteViagem:

    def __init__(self, origem: str, destino: str, duracao: float, custo_unitario: float):
        self.__origem = None
        self.__destino = None
        self.__duracao = None
        self.__custo_unitario = None
        if isinstance(origem, str):
            self.__origem = origem
        if isinstance(destino, str):
            self.__destino = destino
        if isinstance(duracao, float):
            self.__duracao = duracao
        if isinstance(custo_unitario, float):
            self.__custo_unitario = custo_unitario

    @property
    def origem(self):
        return self.__origem
    
    @origem.setter
    def origem(self, origem: str):
        if isinstance(origem, str):
            self.__origem = origem
    
    
    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self, destino: str):
        if isinstance(destino, str):
            self.__destino = destino
            

    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.setter
    def duracao(self, duracao: float):
        if isinstance(duracao, float):
            self.__duracao = duracao
    
    
    @property
    def custo_unitario(self):
        return self.__custo_unitario
    
    @custo_unitario.setter
    def custo_unitario(self, custo_unitario: float):
        if isinstance(custo_unitario, float):
            self.__custo_unitario = custo_unitario