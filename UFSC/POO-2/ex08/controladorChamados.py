from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico

class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__tipos_chamados = []
        self.__chamados = []

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados
        
    @property
    def chamados(self):
        return self.__chamados

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str):
        for tipos_chamados in self.__tipos_chamados:
            if (tipos_chamados.codigo == codigo and tipos_chamados.descricao == descricao and
            tipos_chamados.nome == nome):
                return tipos_chamados
                
        novo_tipo = TipoChamado(codigo, descricao, nome)
        self.__tipos_chamados.append(novo_tipo)
        return novo_tipo

    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
        for chamado in self.__chamados:
            if (chamado.data == data and chamado.cliente == cliente and
            chamado.tecnico == tecnico and chamado.tipo == tipo):
                return chamado
        
        novo_chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
        self.__chamados.append(novo_chamado)
        return novo_chamado

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        return sum(1 for chamado in self.__chamados if chamado.tipo == tipo)

    def relatorio_chamados_atrasados(self):
        atrasados_por_tipo = {}
        hoje = Date.today()

        for chamado in self.__chamados:
            if chamado.prazo < hoje:
                tipo_nome = chamado.tipo.nome
                atrasados_por_tipo[tipo_nome] = atrasados_por_tipo.get(tipo_nome, 0) + 1

        return atrasados_por_tipo
