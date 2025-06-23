from entidade.membro_academia import MembroAcademia

class Ator(MembroAcademia):
    
    def __init__(self, id, nome, data_de_nascimento, nacionalidade):
        super().__init__(id, nome, data_de_nascimento, nacionalidade)