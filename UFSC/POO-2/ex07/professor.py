from funcionario import Funcionario

class Professor(Funcionario):
    
    def __init__(self, departamento, cpf):
        super().__init__(self.departamento, self.cpf, self.dias_de_emprestimo)
    
    def emprestar(self, titulo_livro: str):
        return f'Emprestar {titulo_livro}, com {self.dias_de_emprestimo} de prazo.'
    
    def devolver(self, titulo_livro: str):
        return f'Devolveu {titulo_livro}.'