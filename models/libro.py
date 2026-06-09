class Libro:

    #Constructor
    def __init__(self, id_libro, titulo, autor,isbn):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True #Por defecto el libro esta disponible


    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
    
    def devolver(self):
        self.disponible = True

    def mostrar_info(self):
        return f"Libro ID: { self.id_libro}, Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {'Si' if self.disponible else 'No'}"