from classes import ProcessadorDeArquivo

class ProcessadorCSV(ProcessadorDeArquivo):

    def lerArquivo(self, caminho: str) -> str:
        print(f"CSV: Lendo o arquivo em {caminho}.")
        return "Col 1, Col 2, Col 3"
    
    def analisarConteudo(self, conteudo: str) -> list:
        print(f"CSV: Analisando conteúdo: {conteudo}")
        registros = conteudo.split(',')
        return registros
    
    def processar(self, caminho):
        print("--- Processando o arquivo ---")
        conteudo = self.lerArquivo(caminho)
        registros = self.analisarConteudo(conteudo)
        self.salvarnobanco(registros)
        print(f"Processados {len(registros)} registros.")
        return True
    
class ProcessadorTXT(ProcessadorDeArquivo):
        
    def lerArquivo(self, caminho: str) -> str:
        print(f"TXT: Lendo o arquivo em {caminho}")
        return "Texto"

    def analisarConteudo(self, conteudo: str) -> list:
        print(f"TXT: Analisando conteúdo: {conteudo}")
        registros = conteudo    #Eu nao entendi, o que é para fazer aqui. 
        return registros
    
    def processar(self, caminho):
        print("--- Processando o arquivo ---")
        conteudo = self.lerArquivo(caminho)
        registros = self.analisarConteudo(conteudo)
        self.salvarnobanco(registros)
        print(f"Processados {len(registros)} registros.")
        return True
