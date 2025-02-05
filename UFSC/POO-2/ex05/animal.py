

class Animal(ABC):
	def __init__(self, tamanho_passo: int):
		...

	
	"""Insira aqui os outros metodos"""
	
	@abstractmethod
	def produzir_som(self):
		pass