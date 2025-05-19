from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado):
        if isinstance(data, Date):
            self.data = data
        if isinstance(cliente, Cliente):
            self.cliente = cliente
        if isinstance(tecnico, Tecnico):
            self.tecnico = tecnico
        if isinstance(titulo, str):
            self.titulo = titulo
        if isinstance(descricao, str):
            self.descricao = descricao
        if isinstance(prioridade, int):
            self.prioridade = prioridade
        if isinstance(tipo, TipoChamado):
            self.tipo = tipo
            
    @property
    def data(self):
        return self.data
    
    @property
    def cliente(self):
        return self.cliente
    
    @property
    def tecnico(self):
        return self.tecnico
    
    @property
    def titulo(self):
        return self.titulo
    
    @property
    def descricao(self):
        return self.descricao
    
    @property
    def prioridade(self):
        return self.prioridade
    
    @property
    def tipo(self):
        return self.tipo