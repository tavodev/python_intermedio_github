class MyPostgreSQLConn:
    def __init__(self, bd, user, password, host='127.0.0.1'):
        self.bd = bd
        self.user = user
        self.password = password
        self.host = host

    def connect(self):
        if self.bd and self.user and self.password:
            print(f"Conectado a la base de datos {self.bd}")
            return True
        else:
            return False

    def execute(self, query):
        print("Ejecutando en la bd")
        print(query)

connection = MyPostgreSQLConn("python_intermedio_bd", "postgres", "root")

connection.connect()

connection.execute("SELECT * FROM usuarios;")

lista_ids = [15,20, 30] # estos se borraran

for id in lista_ids:
    connection.execute(f"DELETE FROM usuario WHERE id='{id}';")

