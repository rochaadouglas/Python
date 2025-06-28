from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []
    
    @property
    def clientes(self):
        return self.__clientes
    
    @property
    def tecnicos(self):
        return self.__tecnicos
    
    def inclui_cliente(self, codigo :int, nome :str):
        novo_cliente = Cliente(nome, codigo)
        self.__clientes.append(novo_cliente)
        return novo_cliente
    
    def inclui_tecnico(self, codigo :int, nome :str):
        novo_tecnico = Tecnico(nome, codigo)
        self.__tecnicos.append(novo_tecnico)
        return novo_tecnico