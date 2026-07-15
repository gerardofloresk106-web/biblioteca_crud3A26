#import flet as ft
#from ui.main_window import main_window
from dao.libro_dao import LibroDAO
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO

import flet as ft
from ui.main_window import MainWindow

def main(page: ft.Page):
    page.title = "Sistema de Biblioteca 2026"
    page.window_width = 800
    page.window_height = 600
    page.padding = 0

    interfaz = MainWindow(page)
    menu_visual = interfaz.inicializar_interfaz()
    page.add(menu_visual)

if __name__ == "__main__":
    ft.app(target=main)

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
    titulo = input("Escribe el título del nuevo libro: ")
    autor = input("Escribe el id de autor: ")
    isbn = input("Escribe el isbn del nuevo libro: ") 
    disponible = True
    try:
        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Inserción realizada con éxito")
    except Exception as e:
        print("Error al insertar un nuevo libro")
        print(e)

def actualizar_libro():
    print("Selecciona el libro a actualizar ")
    try:
        libro_dao = LibroDAO()
        ver_libros()
        id = int(input("Escribe el id del libro a actualizar: "))
        titulo = input("Escribe el nuevo título:")
        autor = input("Escribe el nuevo autor: ")
        isbn = input("Escribe el nuevo ISBN: ")
        disponible = bool(input("Escribe el nuevo valor de disponible: "))
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print(f"El libro {id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al actualizar el libro" )
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles")
        ver_libros()
        id = int(input("Escribe el id del libro a eliminar: "))
        libro_dao.eliminar(id)
        print(f"El libro {id} se ha eliminado exitosamente")
    except Exception as e:
        print(f"Error al eliminar el libro {id}")
        print(e)

# ==========================================
# 1. FLUJO DE ADMINISTRADOR (Tu código actual)
# ==========================================
def menu_libros():
    print("\n=== MENÚ ADMINISTRADOR - BIBLIOTECA ===")
    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro")
    print("3. Actualizar un libro disponible")
    print("4. Eliminar un libro disponible")
    print("5. Lista de usuarios")
    print("6. Crear un usuario nuevo")
    print("7. Eliminar un registro de usuarios")
    print("8. Editar un registro de usuarios")
    print("9. Salir del menú de administrador")

    
    try:
        opcion = int(input("Selecciona una opción (1-9): "))
        match opcion:
            case 1: ver_libros()
            case 2: insertar_libro()
            case 3: actualizar_libro()
            case 4: eliminar_libro()
            case 5: listar_usuarios_sistema()
            case 6: crear_usuario()
            case 7: eliminar_usuario()
            case 8: editar_usuario()
            case 9:
                print("Saliendo del menú de administrador...")
            case _: print("Opción no válida.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# (Aquí van tus funciones: ver_libros(), insertar_libro(), etc.)
def crear_usuario():
    print("\n--- CREAR NUEVO USUARIO ---")
    matricula = input("Matrícula del usuario: ")
    nombre = input("Nombre del usuario: ")
    correo = input("Correo electrónico: ")
    # Asegúrate de ingresar un número entero cuando ejecutes el programa
    carrera = int(input("ID numérico de la Carrera: ")) 
    
    try:
        UsuarioDAO.insertar(matricula, nombre, correo, carrera)
        print(f"Usuario '{nombre}' creado con éxito.")
    except Exception as e:
        print(f"Error al crear el usuario: {e}")

def eliminar_usuario():
    print("\n--- ELIMINAR REGISTRO DE USUARIO ---")
    try:
        id_usuario = int(input("Introduce el ID del usuario a eliminar: "))
        UsuarioDAO.eliminar(id_usuario)
        print("Usuario eliminado con éxito.")
    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")

def editar_usuario():
    print("\n--- EDITAR REGISTRO DE USUARIO ---")
    try:
        id_usuario = int(input("Introduce el ID del usuario a modificar: "))
        nombre = input("Nuevo nombre: ")
        correo = input("Nuevo correo electrónico: ")
        carrera = input("Nueva carrera: ")
        
        UsuarioDAO.actualizar(id_usuario, nombre, correo, carrera)
        print("Usuario actualizado con éxito.")
    except Exception as e:
        print(f"Error al actualizar el usuario: {e}")
# ==========================================
# 2. FLUJO DE USUARIOS (Nuevo menú)
# ==========================================
def menu_usuario():
    while True:
        print("\n=== MENÚ DE USUARIO - BIBLIOTECA ===")
        print("1. Ver catálogo de libros disponibles")
        print("2. Buscar un libro")
        print("3. Solicitar préstamo")
        print("4. Ver mis libros prestados")
        print("5. Regresar al menú de inicio") # Cambiado para poder volver
        
        try:
            opcion = int(input("\nSelecciona una opción (1-5): "))
            match opcion:
                case 1:ver_libros_disponibles()
                case 2: buscar_libro()
                case 3: solicitar_prestamo()
                case 4: ver_mis_prestamos()
                case 5: 
                    print("Regresando...")
                    break # Sale del menú de usuario y vuelve al inicio
                case _: print("Opción no válida.")
        except ValueError:
            print("Error: Introduce un número entero válido.")

def listar_usuarios_sistema():
    print("\n--- LISTA DE USUARIOS ---")
    try:
        usuarios = UsuarioDAO.obtener_todos()
        
        if not usuarios:
            print("No hay usuarios registrados en el sistema.")
            return
            
        for u in usuarios:
            # Imprime cada usuario (u[0]=id, u[1]=nombre, u[2]=correo, u[3]=carrera)
            print(f"ID: {u[0]} | Nombre: {u[1]} | Correo: {u[2]} | Carrera: {u[3]}")
            
    except Exception as e:
        print(f"Error al listar los usuarios: {e}")

# (Aquí van tus funciones de usuario: ver_libros_disponibles(), etc.)
def ver_libros_disponibles():
    try:
        # Usamos tu clase DAO que ya maneja la conexión
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todos()
        
        print("\n=== CATÁLOGO DE LIBROS DISPONIBLES ===")
        
        # Variable para controlar si hay libros con estatus disponible
        hay_disponibles = False
        
        if len(libros) == 0:
            print("No hay libros registrados en el sistema.")
        else:
            for libro in libros:
                # NOTA: Cambia 'disponible' por el nombre exacto de la propiedad 
                # o columna que indica si se puede prestar (ej. True o 'Si')
                if libro.disponible == True: 
                    print(f"ID: {libro.id} | Título: {libro.titulo} | Autor: {libro.autor}")
                    hay_disponibles = True
            
            if not hay_disponibles:
                print("Lo sentimos, todos los libros están prestados en este momento.")
                
    except Exception as e:
        print(f"Error al cargar los libros: {e}")
        
    input("\nPresiona Enter para continuar...")


def buscar_libro():
    print("\n--- BUSCAR UN LIBRO ---")
    termino = input("Introduce el título o autor a buscar: ").strip().lower()
    
    try:
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todos() # Traemos la lista de objetos Libro
        
        encontrados = False
        print("\nResultados de la búsqueda:")
        
        for libro in libros:
            # Buscamos coincidencias en el título o autor (en minúsculas)
            if termino in libro.titulo.lower() or termino in libro.autor.lower():
                estado = "Disponible" if libro.disponible else "Prestado"
                print(f"ID: {libro.id} | Título: {libro.titulo} | Autor: {libro.autor} [{estado}]")
                encontrados = True
                
        if not encontrados:
            print("No se encontraron libros que coincidan con la búsqueda.")
            
    except Exception as e:
        print(f"Error al realizar la búsqueda: {e}")
        
    input("\nPresiona Enter para continuar...")


def solicitar_prestamo():
    print("\n--- SOLICITAR PRÉSTAMO ---")
    try:
        id_libro = int(input("Introduce el ID del libro que deseas solicitar: "))
        libro_dao = LibroDAO()
        
        # 1. Buscamos si el libro existe y está disponible
        libros = libro_dao.obtener_todos()
        libro_encontrado = None
        
        for libro in libros:
            if libro.id == id_libro:
                libro_encontrado = libro
                break
                
        if libro_encontrado:
            if libro_encontrado.disponible:
                # 2. Cambiamos su estado a False (No disponible)
                libro_encontrado.disponible = False
                
                # 3. Lo actualizamos en la base de datos usando tu método del DAO
                # NOTA: Asegúrate de tener un método 'actualizar' en tu LibroDAO
                libro_dao.actualizar_libro(libro_encontrado) 
                
                print(f"¡Éxito! Has solicitado el libro: '{libro_encontrado.titulo}'.")
            else:
                print("Lo sentimos, este libro ya se encuentra prestado.")
        else:
            print("El ID ingresado no corresponde a ningún libro.")
            
    except ValueError:
        print("Error: El ID debe ser un número entero.")
    except Exception as e:
        print(f"Error al procesar el préstamo: {e}")
        
    input("\nPresiona Enter para continuar...")


def ver_mis_prestamos():
    print("\n--- MIS LIBROS PRESTADOS ---")
    try:
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todos()
        
        print("\nLibros que tienes bajo tu cuidado:")
        # NOTA: Si aún no tienes un sistema de usuarios/sesiones, esta función de 
        # momento te mostrará todos los libros que están en estado 'Prestado' (disponible = False)
        hay_prestados = False
        
        for libro in libros:
            if not libro.disponible:
                print(f"ID: {libro.id} | Título: {libro.titulo} | Autor: {libro.autor}")
                hay_prestados = True
                
        if not hay_prestados:
            print("No tienes ningún libro prestado actualmente.")
            
    except Exception as e:
        print(f"Error al consultar tus préstamos: {e}")
        
    input("\nPresiona Enter para continuar...")

# ==========================================
# 3. MENÚ PRINCIPAL DE ACCESO
# ==========================================
def menu_principal():
     while True:
         print("\n====== BIENVENIDO A LA BIBLIOTECA ======")
         print("1. Entrar como Administrador")
         print("2. Entrar como Usuario")
         print("3. Salir del sistema")
        
         try:
             rol = int(input("\nSelecciona tu tipo de perfil (1-3): "))
             match rol:
                 case 1:
                     menu_libros() # Llama a tu menú original
                 case 2:
                     menu_usuario() # Llama al nuevo menú
                 case 3:
                     print("¡Sistema cerrado con éxito! Hasta luego.")
                     break # Termina el programa por completo
                 case _:
                     print("Opción incorrecta. Elige 1, 2 o 3.")
         except ValueError:
             print("Error: Ingresa un número válido.")


# ==========================================
# 4. PUNTO DE ENTRADA ÚNICO
# ==========================================

# ft.app(target=main)

if __name__ == "__main__":
     menu_principal() # Arranca siempre desde el selector de roles
