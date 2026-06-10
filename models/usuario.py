class Usuario:

    #Constructor
    def __init__(self, id_usuario, nombre, matricula, email, carrera):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.matricula = matricula
        self.email = email
        self.carrera = carrera
        self.activo = True

    def activar(self):
        self.activo = True

    def descativar(self):
        self.activo = False

    def mostrar_info(self):
        return f"Usuario ID: {self.id_usuario}, Nombre: {self.nombre}, Email: {self.email}, Carrera: {self.carrera}, Activo: {'Si' if self.activo else 'No'}"