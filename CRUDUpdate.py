import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Atualizar dados em uma tabela
sql = "UPDATE clientes SET nome = %s WHERE id = %s"
valores = ("Novo Nome", 1)  # Supondo que queremos atualizar o registro com id 1

cursor.execute(sql, valores)

conexao.commit()

print(cursor.rowcount, "registro(s) atualizado(s).")

conexao.close()
