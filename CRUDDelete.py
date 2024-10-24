import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Excluir dados de uma tabela
sql = "DELETE FROM clientes WHERE id = %s"
valores = (1,)  # Supondo que queremos excluir o registro com id 1

cursor.execute(sql, valores)

conexao.commit()

print(cursor.rowcount, "registro(s) excluído(s).")

conexao.close()
