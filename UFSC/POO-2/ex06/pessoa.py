class Pessoa:
    
    def __init__(self, nome: str, cpf: str):
        self.__nome = None
        self.__cpf = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cpf, str):
            self.__cpf = cpf