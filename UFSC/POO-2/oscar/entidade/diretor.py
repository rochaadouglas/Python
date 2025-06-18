from entidade.membro_academia import MembroAcademia

class Diretor(MembroAcademia):
    
    def __init__(self, id, nome, data_nascimento, nacionalidade):
        super().__init__(id, nome, data_nascimento, nacionalidade)