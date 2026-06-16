#DAO: Data Access Object
# libro_dao.py: objeto de acceso a dotos de la tabla libro
from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

    # SELECT * from libro
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM libro")
        registros = cursor.fetchall()
        libros = []
        for registro in registros:
            libro =libro( 
            registro.id,    
            registro.titulo,
            registro.autor,
            registro.ibsn,
            registro.disponible)
            libros.append(libro)
        cursor.close()
        conexion.close()
        return libros

    def insertar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO libro (titulo, autor, ibsn, disponible) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (libro.titulo, libro.autor, libro.ibsn, libro.disponible))
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE libro SET titulo = %s, autor = %s, ibsn = %s, disponible = %s WHERE id = %s"
        cursor.execute(sql, (libro.titulo, libro.autor, libro.ibsn, libro.disponible, libro.id))
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, libro_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execuete("DELETE FROM libro WHERE id = %s", (libro_id,))
        conexion.commit()
        cursor.close()
        conexion.close()