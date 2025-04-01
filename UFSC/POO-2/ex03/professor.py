from ex03 import Aluno
class Professor:
    
    def __init__(self, nome: str, endereco: str, orientando: Aluno):
        self.__nome = None
        self.__endereco = None
        self.__orientando = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(endereco, str):
            self.__endereco = endereco
        if isinstance(orientando, Aluno):
            self.__orientando = orientando
            
    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
            
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco
            
    @property
    def orientando(self):
        return self.__orientando
    
    @orientando.setter
    def orientando(self, orientando: Aluno):
        if isinstance(orientando, Aluno):
            self.__orientando = orientando

al = Aluno("Marcos", "Centro")
prof = Professor("Douglas", "Trindade", al)
print(prof.orientando.nome)
print(prof.orientando.endereco)