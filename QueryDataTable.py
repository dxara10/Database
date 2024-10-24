import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Consultar dados de uma tabela
sql = "SELECT * FROM tabela"

cursor.execute(sql)

resultados = cursor.fetchall()

for resultado in resultados:
    print(resultado)

conexao.close()
