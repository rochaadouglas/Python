class Pessoa():

    def __init__(self, cpf='000.000.000-00', nome='___'):
        self._cpf = cpf
        self.nome = nome
         
class Estudante(Pessoa):

    def __init__(self, cpf='000.000.000-00', nome='___', matricula=''):
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
        novo_estudante = Estudante(cpf, nome, matricula)
        if matricula not in self.__cad:
            self.__cad[matricula] = novo_estudante
            return True
        else:
            return False
        
estudante = Cadastro()
print(estudante.adicionaEstudante('000.000.000-00', 'Fulano de tal', '20203711'))
print(estudante.adicionaEstudante('000.000.000-00', 'Fulano de tal', '20203711'))

print('---'*30)

def verifica_pixel_esquerda(matriz, linha=2, coluna=2):
    tam = len(matriz)
    l = linha
    while l >= 0:
        qtcol = len(matriz[l])
        col = coluna
        while col < qtcol:
            elemento = matriz[l][col]
            if elemento != 0:
                print(elemento)
            col += 1
        l -= 1

def verifica_pixel_direita(matriz):
    pass


m = [[0, 0, 0, 0, 0],
     [0, 0, 0, 7, 0],
     [0, 0, 7, 7, 7],]

verifica_pixel_esquerda(m)