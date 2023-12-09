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
fulano.__str__()
