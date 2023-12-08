class Pessoa():

    def __init__(self, cpf='000.000.000-00', nome='___'):
        self.cpf = cpf
        self.nome = nome
        
    def exibir(self):
        print('------------')
        print(self.cpf, self.nome)

class Estudante(Pessoa):

    def __init__(self, cpf='000.000.000-00', nome='___', matricula=''):
        super().__init__(cpf, nome)
        self.matricula = matricula

    def exibir(self):
        Pessoa.exibir(self)
        print(self.matricula)


obj1 = Estudante()
print(f'{obj1.cpf}')

joo = Estudante('000.0000.1212', 'joo', 'eofefoe')
joo.exibir()

