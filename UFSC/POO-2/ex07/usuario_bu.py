from abc import ABC, abstractmethod

class UsuarioBU(ABC):
    
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int):
        self.__cpf = None
        self.__dias_de_emprestimo = None
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo
            
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: int):
        if isinstance(cpf, int):
            self.__cpf = cpf
            
    @property
    def dias_de_emprestimo(self):
        return self.__dias_de_emprestimo
    
    @dias_de_emprestimo.setter
    def dias_de_emprestimo(self, dias_de_emprestimo: int):
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo
    
    @abstractmethod        
    def emprestar(self, titulo_livro: str):
        return f'Emprestar {titulo_livro}, com {self.dias_de_emprestimo} de prazo.'
    
    @abstractmethod
    def devolver(self, titulo_livro: str):
        return f'Devolveu {titulo_livro}'