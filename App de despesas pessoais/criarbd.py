#TIME: 18:40

# importando SQLite
import sqlite3 as lite

# Criando coexão com o banco de dados
con = lite.connect('dados.db')

# Criando tabela de categorias
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

# Criando tabela de receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

# Criando tabela de despesas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")