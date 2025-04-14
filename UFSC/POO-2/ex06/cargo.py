class Cargo:
    
    def __init__(self, salario: int, descricao: str):
        self.__salario = None
        self.__descricao = None
        if isinstance(salario, int):
            self.__salario = salario 
        if isinstance(descricao, str):
            self.__descricao = descricao