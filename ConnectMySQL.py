import mysql.connector

# Estabelecer conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

# Verificar se a conexão foi bem sucedida
if conexao.is_connected():
    print("Conexão bem sucedida ao banco de dados MySQL.")
else:
    print("Falha ao conectar ao banco de dados MySQL.")
