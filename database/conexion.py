import psycopg2

class Conexion:

    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(
        host = "localhost",
        database = "biblioteca_3a26",
        user = "postgres",
        password = "Fenix306"
        port = "5432"

    )
    