from entidade.membro_academia import MembroAcademia

class Ator(MembroAcademia):
    
    def __init__(self, id: int, nome: str, data_de_nascimento: str, nacionalidade: str):
        super().__init__(id, nome, data_de_nascimento, nacionalidade)