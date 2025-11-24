from abc import abstractmethod, ABC
from fmethod import Transporte, Navio, Caminhão

class Logistica(ABC):

    @abstractmethod
    def criar_transporte(self) -> Transporte:
        pass

    def planejar_entrega(self) -> str:
        print("Logística: Iniciando o planejamento")
        transporte = self.criar_transporte()
        resultado = transporte.entregar()
        print(f"{transporte.entregar()}")
        print(f"Processado finalizado.")
        return resultado
    
class LogisticaTerrestre(Logistica):

    def criar_transporte(self) -> Transporte:
        print("Tranporte Terrestre: O meio de transporte solicitado foi o caminhão.")
        return Caminhão()
    
class LogisticaMarítima(Logistica):

    def criar_transporte(self) -> Transporte:
        print("Tranporte Marítimo: O meio de transporte solicitado foi o Navio.")
        return Navio()
        

