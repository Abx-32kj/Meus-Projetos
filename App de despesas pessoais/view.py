#TIME: 51:00

import sqlite3 as lite

# Criando coexão com o banco de dados
con = lite.connect('dados.db')

#Funções de inserção -------------------------------------------------

# Operação de incerir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)

# Operação de incerir receitas
def inserir_receitas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# Operação de incerir despesas
def inserir_despesas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

#Funções para deletar -------------------------------------------------

#Deletar receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id = ?"
        cur.execute(query, i)

#Deletar gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id = ?"
        cur.execute(query, i)

#Funções para visualizar dados ------------------------------------------

#Visualizar categorias
def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Visualizar receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens 

# Visualizar Gastos
def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens 





#Função para deletar categoria pelo id (caso precise)
'''def deletar_categoria(id_categoria):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Categoria WHERE id = ?"
        cur.execute(query, (id_categoria,))
        
        deletar_categoria(3)'''