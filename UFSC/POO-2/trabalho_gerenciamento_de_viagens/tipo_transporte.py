class TipoTransporte:
    
    def __init__(self, tipo_veiculo: str, modelo_veiculo: str, placa_veiculo: str):
        self.__tipo_veiculo = None
        self.__modelo_veiculo = None
        self.__placa_veiculo = None
        
        if isinstance(tipo_veiculo, str):
            self.__tipo_veiculo = tipo_veiculo
        if isinstance(modelo_veiculo, str):
            self.__modelo_veiculo = modelo_veiculo
        if isinstance(placa_veiculo, str):
            self.__placa_veiculo = placa_veiculo
            
            
    @property
    def tipo_veiculo(self):
        pass