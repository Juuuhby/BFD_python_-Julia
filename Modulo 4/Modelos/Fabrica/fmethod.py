from abc import ABC, abstractmethod

class Transporte(ABC):

    @abstractmethod
    def entregar(self) -> str:
        pass

class Caminhão(Transporte):

    def entregar(self) -> str:
        return "Entrega por Terra: O caminhão está transportando a mercadoria."
        

class Navio(Transporte):

    def entregar(self) -> str:
        return "Entrega pelo Mar: O navio está transportando a carga."
        
