

class Cliente:

    def __init__(self, nome = str, fone = str):
        self.__nome = None
        self.__fone = None
        
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(fone, str):
            self.__fone = fone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome = str):
        if isinstance(nome, str):
            self.__nome = nome
            
    
    @property
    def fone(self):
        return self.__fone
    
    @fone.setter
    def fone(self,fone = str):
        if isinstance(fone, str):
            self.__fone = fone