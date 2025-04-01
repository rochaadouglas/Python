

class Cliente:

    def __init__(self, nome: str, fone: int, email: str):
        self.__nome = None
        self.__fone = None
        self.__email = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(fone, int):
            self.__fone = fone
        if isinstance(email, str):
            self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    
    @property
    def fone(self):
        return self.__fone
    
    @fone.setter
    def fone(self, fone: int):
        if isinstance(fone, int):
            self.__fone = fone
    
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        if isinstance(email, str):
            self.__email = email