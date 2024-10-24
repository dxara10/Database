import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Inserir dados em uma tabela
sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
valores = ("Novo Cliente", "novo_cliente@example.com")

cursor.execute(sql, valores)

conexao.commit()

print(cursor.rowcount, "registro(s) inserido(s).")

conexao.close()
