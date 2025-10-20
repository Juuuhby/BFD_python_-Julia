import sqlite3

con = sqlite3.connect("tabela.db")

cursor = con.cursor()

print("Bancos de Dados criado!")