import sqlite3

con = sqlite3.connect("tabela.db")

cursor = con.cursor()

print("Bancos de Dados criado!")

cursor.execute("""CREATE TABLE IF NOT EXISTS clientes(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               profissão TEXT NOT NULL,
               telefone TEXT NOT NULL,
               estado TEXT NOT NULL); """)

print("Tabela criada com sucesso!")

con.commit()

cursor.execute("INSERT INTO clientes (nome, profissão, telefone, estado) VALUES (?,?,?,?)",
               ("Justin Bieber", "Cantor", "(21) 99999-9999", "California" ))

cursor.execute("INSERT INTO clientes (nome, profissão, telefone, estado) VALUES (?,?,?,?)",
               ("Ariana Grande", "Cantora/Atriz", "(22) 88888-8888", "California"))

cursor.execute("INSERT INTO clientes (nome, profissão , telefone, estado) VALUES (?,?,?,?)",
               ("Michael Jordan","Ator", "(21)77777-7777", "Florida"))

cursor.execute("INSERT INTO clientes (nome, profissão , telefone, estado) VALUES (?,?,?,?)",
               ("Sabrina Carpenter", "Cantora/Atriz", "(24)66666-6666", "California"))

print("Os clientes foram adicionados na tabela!")

con.commit()

cursor.execute("SELECT * FROM clientes")
result = cursor.fetchall()

print("--- Lista de Clientes ---")
for i in result:
    print(f"Id: {i[0]}, Nome: {i[1]}, Profissão: {i[2]}, Número: {i[3]}, Estado: {i[4]}.")
    print("---"*10)

con.close()