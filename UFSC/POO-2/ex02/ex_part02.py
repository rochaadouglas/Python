class Aluno:
    
    def __init__(self, nome, idade: int, matricula):
        self.__nome = nome
        if isinstance(idade, int):
            self.__idade = idade
        self.__matricula = matricula
        
    
    def mostra_dados(self):
        print("seu nome é:", self.__nome)
        print("sua idade é:", self.__idade)
        print("sua matricula é:", self.__matricula)
    
    def faz_aniversario(self):
        self.__idade = self.__idade + 1
    
al = Aluno("Douglas", 29, 123411)
al.faz_aniversario()
al.mostra_dados()