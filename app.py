from dao.libro_dao import LibroDAO
from models.libro import Libro

def ver_libros():   
    try:
        libro_dao = LibroDAO()

        libros = libro_dao.obtener_todos()

        print ("=== Libros en la biblioteca ===")

        if len(libros) == 0:
            print ("No hay libros registrados.")
        else:
            for libro in libros:
                print ("--------------------------------------")

                print (
                    f"ID: {libro.id}, Título: {libro.titulo},"
                    f" Autor: {libro.autor}, ISBN: {libro.isbn},"
                    f" Disponible: {'Si' if libro.disponible else 'No'}"
                )
                print ("--------------------------------------")
        print("\n Conexion exitosa a ala base de datos")
    except Exception as e:
        print ("Error: ")
        print(e)

def insertar_libro():
        titulo = input("Ingrese el título de un nuevo libro: ")
        autor = input("Ingrese el id del autor: ")
        isbn = input("Ingrese el ISBN del nuevo libro: ")
        disponible = True
        try:
             libro_dao = LibroDAO()
             id = libro_dao.obtener_ultimo_id() + 1
             libro = Libro(id, titulo, autor, isbn, disponible)
             libro_dao.insertar(libro)
             print("Libro insertado exitosamente.")
        except Exception as e:
            print("Error al insertar el libro:")
            print(e) 

def main():
     print("=== BIBLIOTECA UNIVERSITARIA ===")
     print("Menu de opciones")
     print("1. Ver todos los libros")
     print("2. insertar un nuevo libro")
     print("3. Actualizar un libro disponible")
     print("4. Eliminar un libro disponible")
     opcion = int(input("Seleccione una opción (1-4): "))

     match opcion:
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
            print("Opción 2: Insertar un nuevo libro")
        case 3:
            
            print("Opción 3: Actualizar un libro disponible")
        case 4: 
            print("Opción 4: Eliminar un libro disponible")
     
    
if __name__ == "__main__":
    main()