from aluno import Aluno

class AlunoPosGraduacao(Aluno):
    
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int, elaborando_tese: bool):
        super().__init__(self.cpf, self.dias_de_emprestimo, self.matricula)
        if isinstance(cpf, int):
            self.cpf = cpf
        if isinstance(dias_de_emprestimo, int):
            self.dias_de_emprestimo = dias_de_emprestimo
        if isinstance(matricula, int):
            self.matricula = matricula
        if isinstance(elaborando_tese, bool):
            self.__elaborando_tese = elaborando_tese
            
    
    @property
    def elaborando_tese(self):
        return self.__elaborando_tese
    
    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese: bool):
        if isinstance(elaborando_tese, bool):
            self.__elaborando_tese = elaborando_tese
            
    def emprestar(self, titulo_livro: str):
        return f'Emprestar {titulo_livro}, com {self.dias_de_emprestimo} de prazo.'
    
    def devolver(self, titulo_livro: str):
        return f'Devolveu {titulo_livro}.'
    

al01 = AlunoPosGraduacao(12032, 30, 232323, True)
print(al01.emprestar("Harry Poter"))