class EmpresaTransporte:
    
    def __init__(self,id_empresa: int, nome: str, cnpj: str, telefone: str):
        self.__id_empresa = None
        self.__nome = None
        self.__cnpj = None
        self.__telefone = None
        
        if isinstance(id_empresa, int):
            self.__id_empresa = id_empresa
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
        if isinstance(telefone, str):
            self.__telefone = telefone
            
            
    @property
    def id_empresa(self):
        return self.__id_empresa
    
    @id_empresa.setter
    def id_empresa(self, id_empresa: int):
        if isinstance(id_empresa, int):
            self.__id_empresa = id_empresa
            
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
            
            
    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj: str):
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
            
            
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone