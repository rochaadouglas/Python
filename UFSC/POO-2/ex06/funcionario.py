from cargo import Cargo
from pessoa import Pessoa
from dependente import Dependente

class Funcionario(Pessoa): 
    
    def __init__(self, cargo: Cargo, nome: str, cpf: str):
        super().__init__(nome, cpf)
        if isinstance(cargo, Cargo):
            self.__cargo = cargo
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cpf, str):
            self.__cpf = cpf
        self.__dependentes = []
        
        
    def add_dependente(self, nome: str, cpf: str):
        dependente = Dependente(nome, cpf)
        self.__dependentes.append(dependente)
    
    def rem_dependente(self, nome: str, cpf: str):
        dependente = Dependente(nome, cpf)
        self.__dependentes.remove(dependente)