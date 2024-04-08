class Cliente:

    def __init__(self, nome=None, fone=None):
        self.__nome = nome
        self.__fone = fone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome=None):
        self.__nome = nome

    @property
    def fone(self):
        return self.__fone
    
    @fone.setter
    def fone(self, fone=None):
        self.__fone = fone