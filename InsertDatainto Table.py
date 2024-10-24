import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Inserir dados em uma tabela
sql = "INSERT INTO tabela (coluna1, coluna2) VALUES (%s, %s)"
valores = ("valor1", "valor2")

cursor.execute(sql, valores)

conexao.commit()

print(cursor.rowcount, "registro(s) inserido(s).")

conexao.close()
