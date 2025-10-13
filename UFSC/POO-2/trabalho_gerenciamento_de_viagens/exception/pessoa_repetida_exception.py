class PessoaRepetidaException(Exception):
    
    def __init__(self, id):
        self.mensagem = "A pessoa de id {} já está cadastrada."
        super().__init__(self.mensagem.format(id))