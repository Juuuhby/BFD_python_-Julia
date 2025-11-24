from Processador import ProcessadorCSV, ProcessadorTXT

def cliente_processadorcsv(nome_arquivo: str):
    print(f"Cliente: Processando documento '{nome_arquivo}'")
    leitor = ProcessadorCSV()
    status = leitor.processar(nome_arquivo)
    return f"Status final: {status}"

def cliente_processadortxt(nome_arquivo: str):
    print(f"Cliente: Processando documento '{nome_arquivo}'")
    leitor = ProcessadorTXT()
    status = leitor.processar(nome_arquivo)
    return f"Status final: {status}"
 
cliente_processadorcsv(nome_arquivo= "arquivo.csv")
cliente_processadortxt(nome_arquivo= "Arquivo.txt")

    
    