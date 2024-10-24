import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Atualizar dados em uma tabela
sql = "UPDATE tabela SET coluna1 = %s WHERE coluna2 = %s"
valores = ("novo_valor", "valor_atual")

cursor.execute(sql, valores)

conexao.commit()

print(cursor.rowcount, "registro(s) atualizado(s).")

conexao.close()
