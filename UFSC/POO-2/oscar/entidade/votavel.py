from abc import ABC, abstractmethod

class Votavel(ABC):
    @abstractmethod
    def __init__(self, id: int):
        self.__id = id
        
    @property
    def id(self):
        return self.__id