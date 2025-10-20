import sqlite3

con = sqlite3.connect("tabela.db")

cursor = con.cursor()

print("Bancos de Dados criado!")

cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               cpf TEXT NOT NULL,
               telefone TEXT NOT NULL,
               estado TEXT NOT NULL); """)

print("Tabela criada com sucesso!")

con.commit()