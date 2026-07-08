from database.conexion import Conexion

class UsuarioDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM vista_usuarios;") # O la consulta que tenías originalmente
            registros = cursor.fetchall()
            cursor.close()
            return registros
        except Exception as e:
            raise e
        finally:
            if conexion:
                conexion.close()
    
    
    @classmethod
    def insertar(cls, matricula, nombre, correo, carrera):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            
            # Autogeneramos el id numérico
            cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM usuario;")
            nuevo_id = cursor.fetchone()
            
            # ORDEN EXACTO DE TU BASE DE DATOS:
            # Columna 1: id (nuevo_id)
            # Columna 2: nombre (nombre)
            # Columna 3: matricula (matricula)
            # Columna 4: carrera (carrera -> DEBE SER EL ID NUMÉRICO DE LA CARRERA)
            # Columna 5: correo (correo)
            sql = """
                INSERT INTO usuario (id, nombre, matricula, carrera, correo) 
                VALUES (%s, %s, %s, %s, %s);
            """
            valores = (nuevo_id, nombre, matricula, carrera, correo)
            
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
        except Exception as e:
            if conexion:
                conexion.rollback()
            raise e
        finally:
            if conexion:
                conexion.close()

    @classmethod
    def actualizar(cls, id_usuario, nombre, correo, carrera):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            
            sql = "UPDATE usuario SET nombre = %s, correo = %s, carrera = %s WHERE id = %s;"
            valores = (nombre, correo, carrera, id_usuario)
            
            cursor.execute(sql, valores)
            conexion.commit()
            cursor.close()
        except Exception as e:
            if conexion:
                conexion.rollback()
            raise e
        finally:
            if conexion:
                conexion.close()

    @classmethod
    def eliminar(cls, id_usuario):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            
            # Consulta para borrar por ID
            sql = "DELETE FROM usuario WHERE id = %s;"
            cursor.execute(sql, (id_usuario,))
            
            conexion.commit()
            cursor.close()
        except Exception as e:
            if conexion:
                conexion.rollback()
            raise e
        finally:
            if conexion:
                conexion.close()
    
