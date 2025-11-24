from abc import ABC, abstractmethod

class ProcessadorDeArquivo(ABC):

    @abstractmethod
    def lerArquivo(self, caminho: str) -> str:
        pass
    
    @abstractmethod
    def analisarConteudo(self, conteudo: str) -> list:
       pass

    def salvarnobanco(self, registros: list):
        print("---- Iniciando salvamento no Banco de Dados ----")
        print(f"Salvando o registro: {registros} no banco de dados.")
        print("---- Salvamento concluído ---")
        return True
    
    def processar(self,caminho: str) -> str:
        print("--- Processando o arquivo ---")
        conteudo = self.lerArquivo(caminho)
        registros = self.analisarConteudo(conteudo)
        self.alvarnobanco(registros)
        print(f"Processados {len(registros)} registros.")
        return True



