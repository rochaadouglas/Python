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
    
    def inclui_cliente(self, codigo :int, nome :str) -> Cliente:
        cliente = Cliente(nome, codigo)
        if cliente not in self.__clientes:
            self.__clientes.append(cliente)
    
    def inclui_tecnico(self, codigo :int, nome :str) -> Tecnico:
        pass