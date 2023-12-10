class Pessoa():

    def __init__(self, cpf='000.000.000-00', nome='___'):
        self._cpf = cpf
        self.nome = nome
         
class Estudante(Pessoa):

    def __init__(self, cpf='000.000.000-00', nome='___', matricula=' '):
        super().__init__(cpf, nome)
        self.__matricula = matricula
    
    def __str__(self):
        print(f'{self._cpf, self.nome, self.__matricula}')

fulano = Estudante('000.000.000-00', 'Fulano de tal', '20203711')
#fulano.__str__()

class Cadastro():

    def __init__(self):
        self.__cad = {}

    def adicionaEstudante(self, cpf, nome, matricula):
        self.cpf = cpf
        self.nome = nome
        self.matricula = matricula
        if self.matricula not in self.__cad:
            self.__cad = matricula
            return True
        else:
            return False
        
estudante = Cadastro()
estudante.adicionaEstudante({20203711:['']})