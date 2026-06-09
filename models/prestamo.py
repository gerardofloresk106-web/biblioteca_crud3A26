from models.libro import Libro

class Prestamo :

    #Constructor 
    def __init__(self, id_prestamo, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False #Por defecto el prestamo no ha sido devuelto
        
    def registrar_devolucion(self):
        self.devuelto = True
        self.libro.devolver ()

    def mostrar_info(self):
        return f"Préstamo ID: {self.id_prestamo}, Usuario: {self.usuario.nombre}, Libro:{self.libro.titulo}, Fecha prestamo:{self.fecha_prestamo} "