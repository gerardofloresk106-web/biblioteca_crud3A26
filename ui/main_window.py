# import flet as ft

# def main_window(page:ft.Page):
#     page.title = "Sistema de Biblioteca Universitaria"
#     page.window_width = 1100
#     page.window_height = 700
#     page.padding = 0    
#     page.bgcolor = "#f5f5f5"
#     #page.bgcolor = ft.Colors.BLUE_GREY_50
# #titulo y subtitulo de la ventana
#     titulo = ft.Text("Sistema de Biblioteca Universitaria", size=24, weight="bold", color=ft.Colors.BLUE_GREY_900)
# #subtitulo de la ventana
#     subtitulo = ft.Text("Bienvenido al sistema de gestión de biblioteca", size=16, color=ft.Colors.BLUE_GREY_600)
# #widget container para contener el contenido de la ventana
#     contenido = ft.Container(
#     content = ft.Column(
#         controls = [
#             titulo,
#             subtitulo
#             ],
#             spacing = 10,
#     ), 
#     padding = 30,
#     expand = True

#     )

#     menu_lateral = ft.container(
#         width = 220,
#         bgcolor = "blue grey 900",
#         padding = 20,
#         content = ft.Column(
#             controls = [
#                 ft.Text("Biblioteca", size=20, weight="bold", color=ft.Colors.BLUE_GREY_100),
#                 ft.Text("Sistema de gestion", size=12, color=ft.Colors.BLUE_GREY_100),
#                 ft.Divider(color = ft.Colors.BLUE_GREY_700),
#                 ft.ElevatedButton(
#                     "Libros",
#                     icon = ft.icons.PERSON,
#                     width=180,
#                 ),
#                 ft.ElevatedButton(
#                     "Usuarios",
#                     icon = ft.icons.PERSON,
#                     width=180,
#                 ),
#                  ft.ElevatedButton(
#                     "Prestamos",
#                     icon = ft.icons.SWAP_HORIZ,
#                     width=180,
#                 ),
#                 ft.ElevatedButton(
#                     "devoluciones",
#                     icon = ft.icons.KEYBOARD_RETURN,
#                     width=180,
#                 ),
#             ],
#             spacing = 15
#         )
#     )

#     layout = ft.Row(
#         controls = [
#             menu_lateral,
#             contenido
#         ],
#         expand = True
#     )

#     page.add(layout)

#def inicio():
#    contenido.contenido = inicio()
#   page.update

#    def mostrar_insertar_libro


# import flet as ft

# class MainWindow:
#     def __init__(self, page: ft.Page):
#         self.page = page
#         self.contenedor_principal = ft.Container()

#     def inicializar_interfaz(self):
#         self.mostrar_menu_principal()
#         return self.contenedor_principal

#     def mostrar_menu_principal(self):
#         self.contenedor_principal.content = ft.Column(
#             controls=[
#                 # CORRECCIÓN:
#                 ft.Text("====== BIENVENIDO A LA BIBLIOTECA ======", size=20, weight="bold"),
#                 ft.ElevatedButton("1. Entrar como Administrador", on_click=lambda _: self.mostrar_menu_administrador()),
#                 ft.ElevatedButton("2. Entrar como Usuario", on_click=lambda _: self.mostrar_menu_usuario()),
#                 ft.ElevatedButton("3. Salir del sistema", on_click=lambda _: self.page.window_close()),
#             ],
            
#             alignment="center",
#             horizontal_alignment="center"
#         )
#         self.page.update()

#     def mostrar_menu_administrador(self):
        
#         # --- OPCIÓN 1: VER TODOS LOS LIBROS (CONECTADO A VISTA_LIBROS) ---
#         def click_ver_todos_los_libros(e):
#             try:
#                 # 1. Importamos el DAO localmente o arriba en tu archivo
#                 from dao.libro_dao import LibroDAO
                
#                 # 2. Traemos las filas desde pgAdmin
#                 registros = LibroDAO.obtener_todos()
                
#                 # 3. Creamos una tabla para organizar las columnas
#                 tabla_datos = ft.DataTable(
#                     columns=[
#                         ft.DataColumn(ft.Text("ID")),
#                         ft.DataColumn(ft.Text("Título")),
#                         ft.DataColumn(ft.Text("Autor")),
#                         ft.DataColumn(ft.Text("Estado")),
#                     ],
#                     rows=[]
#                 )
                
#                 if not registros:
#                     contenido_pantalla = ft.Text("No hay libros registrados en la base de datos.", color="orange")
#                 else:
#                     # 4. Llenamos las filas según el orden de columnas en tu 'vista_libros'
#                     # Ajusta los índices (u[0], u[1]...) según cómo creaste tu VISTA en SQL
#                     for u in registros:
#                         estado_libro = "Disponible" if u[3] else "Prestado" # Suponiendo que el booleano está en el índice 3
                        
#                         tabla_datos.rows.append(
#                             ft.DataRow(
#                                 cells=[
#                                     ft.DataCell(ft.Text(str(u[0]))), # ID del libro
#                                     ft.DataCell(ft.Text(str(u[1]))), # Título
#                                     ft.DataCell(ft.Text(str(u[2]))), # Autor (Nombre de la vista)
#                                     ft.DataCell(ft.Text(estado_libro, color="green" if u[3] else "red")),
#                                 ]
#                             )
#                         )
#                     # Metemos la tabla dentro de un contenedor con scroll por si son muchos libros
#                     contenido_pantalla = ft.ListView(expand=True, controls=[tabla_datos])
                    
#             except Exception as ex:
#                 contenido_pantalla = ft.Text(f"Error al leer vista_libros: {ex}", color="red")

#             # 5. Redibujamos el contenedor principal con la tabla de datos
#             self.contenedor_principal.content = ft.Column(
#                 controls=[
#                     ft.Text("====== CATÁLOGO DE LIBROS (pgAdmin) ======", size=18, weight="bold"),
#                     ft.Divider(height=10),
#                     contenido_pantalla,
#                     ft.Divider(height=10),
#                     ft.ElevatedButton("Volver al Menú Admin", on_click=lambda _: self.mostrar_menu_administrador())
#                 ],
#                 spacing=10,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER
#             )
#             self.page.update()

#         # --- TU DISEÑO ORIGINAL DEL MENÚ ADMINISTRADOR ACTUALIZADO ---
#         self.contenedor_principal.content = ft.Column(
#             controls=[
#                 ft.Text("====== MENÚ ADMINISTRADOR - BIBLIOTECA ======", size=18, weight="bold"),
                
#                 # REEMPLAZAMOS EL PRINT POR NUESTRA NUEVA FUNCIÓN CONECTADA AL DAO
#                 ft.ElevatedButton("1. Ver todos los libros", on_click=click_ver_todos_los_libros),
                
#                 # Conectado a la función que abre tu archivo independiente libro_form.py
#                 ft.ElevatedButton("2. Insertar un nuevo libro", on_click=lambda _: self.abrir_formulario_libro()),
                
#                 ft.ElevatedButton("3. Actualizar un libro disponible"),
#                 ft.ElevatedButton("4. Eliminar un libro disponible"),
                
#                 # Conectados a tu UsuarioDAO (del paso anterior)
#                 ft.ElevatedButton("5. Lista de usuarios", on_click=lambda _: print("Opción 5 (Ya configurada)")), 
#                 ft.ElevatedButton("6. Crear un usuario nuevo"),
#                 ft.ElevatedButton("7. Eliminar un registro de usuarios"),
#                 ft.ElevatedButton("8. Editar un registro de usuarios"),
#                 ft.ElevatedButton("9. Regresar al menú de inicio", on_click=lambda _: self.mostrar_menu_principal()),
#             ],
#             spacing=10
#         )
#         self.page.update()

#     def mostrar_menu_usuario(self):
#         self.contenedor_principal.content = ft.Column(
#             controls=[
#                 ft.Text("====== MENÚ DE USUARIO - BIBLIOTECA ======", size=18, weight="bold"),
#                 ft.ElevatedButton("1. Ver catálogo de libros disponibles"),
#                 ft.ElevatedButton("2. Buscar un libro"),
#                 ft.ElevatedButton("3. Solicitar préstamo"),
#                 ft.ElevatedButton("4. Ver mis libros prestados"),
#                 ft.ElevatedButton("5. Regresar al menú de inicio", on_click=lambda _: self.mostrar_menu_principal()),
#             ],
#             spacing=10
#         )
#         self.page.update()

import flet as ft
from dao.usuario_dao import UsuarioDAO
from dao.libro_dao import LibroDAO

class MainWindow:
    def __init__(self, page: ft.Page):
        self.page = page
        
        self.page.padding = 0
        self.page.spacing = 0
        self.page.theme_mode = "light"
        
        self.area_contenido = ft.Container(
            expand=True,
            padding=30,
            bgcolor="white", 
            content=ft.Column(controls=[])
        )
        
        self.contenedor_principal = ft.Container(expand=True)

    def inicializar_interfaz(self):
        self.construir_estructura_base()
        self.mostrar_vista_inicio()
        return self.contenedor_principal

    def construir_estructura_base(self):
        # --- MENÚ LATERAL IZQUIERDO (SIDEBAR) ---
        sidebar = ft.Container(
            width=280,
            bgcolor="#4A4A4A", 
            padding=ft.padding.only(top=40, left=20, right=20, bottom=20),
            content=ft.Column(
                controls=[
                    ft.Text("Biblioteca", size=24, weight="bold", color="white"),
                    ft.Text("Sistema de gestión", size=14, color="grey"),
                    ft.Divider(height=30, color="grey"),
                    
                    # Botones adaptados para versiones antiguas (sin 'style' ni 'RoundedRectangleBorder')
                    ft.ElevatedButton(
                        content=ft.Row([ft.Icon("home", color="#4A4A4A"), ft.Text("Inicio", color="#4A4A4A")], spacing=10),
                        bgcolor="white",
                        width=240, height=45, on_click=lambda _: self.mostrar_vista_inicio()
                    ),
                    ft.ElevatedButton(
                        content=ft.Row([ft.Icon("book", color="#4A4A4A"), ft.Text("Libros", color="#4A4A4A")], spacing=10),
                        bgcolor="white",
                        width=240, height=45, on_click=lambda _: self.mostrar_menu_libros()
                    ),
                    ft.ElevatedButton(
                        content=ft.Row([ft.Icon("person", color="#4A4A4A"), ft.Text("Usuarios", color="#4A4A4A")], spacing=10),
                        bgcolor="white",
                        width=240, height=45, on_click=lambda _: self.mostrar_menu_usuarios()
                    ),
                    ft.ElevatedButton(
                        content=ft.Row([ft.Icon("swap_horiz", color="#4A4A4A"), ft.Text("Préstamos", color="#4A4A4A")], spacing=10),
                        bgcolor="white",
                        width=240, height=45
                    ),
                    ft.ElevatedButton(
                        content=ft.Row([ft.Icon("keyboard_return", color="#4A4A4A"), ft.Text("Devoluciones", color="#4A4A4A")], spacing=10),
                        bgcolor="white",
                        width=240, height=45
                    ),
                ],
                spacing=15,
            )
        )

        self.contenedor_principal.content = ft.Row(
            controls=[
                sidebar,
                self.area_contenido
            ],
            expand=True,
            spacing=0
        )

    def mostrar_vista_inicio(self):
        self.area_contenido.content = ft.Column(
            controls=[
                ft.Text("Inicio del Sistema", size=28, weight="bold", color="#4A4A4A"),
                ft.Text("Selecciona una opción del panel izquierdo para comenzar a operar.", size=16, color="grey"),
            ],
            spacing=10
        )
        self.page.update()

    def mostrar_menu_libros(self):
        # Eliminados argumentos de bordes avanzados para máxima compatibilidad
        input_titulo = ft.TextField(label="Título del libro:", width=500)
        input_autor = ft.TextField(label="Autor del libro:", width=500)
        input_isbn = ft.TextField(label="ISBN:", width=500)
        text_mensaje = ft.Text("")

        def ejecutar_guardado(e):
            if not input_titulo.value or not input_autor.value:
                text_mensaje.value = "Por favor, llena los campos básicos."
                text_mensaje.color = "orange"
                self.page.update()
                return
            try:
                LibroDAO.insertar(titulo=input_titulo.value, id_autor=int(input_autor.value))
                text_mensaje.value = "¡Libro registrado exitosamente en pgAdmin!"
                text_mensaje.color = "green"
                input_titulo.value = ""
                input_autor.value = ""
                input_isbn.value = ""
            except Exception as ex:
                text_mensaje.value = f"Error en BD: {ex}"
                text_mensaje.color = "red"
            self.page.update()

        self.area_contenido.content = ft.Column(
            controls=[
                ft.Text("Registrar nuevo libro", size=26, weight="bold", color="#4A4A4A"),
                ft.Text("Capture los datos básicos del libro", size=14, color="grey"),
                ft.Divider(height=20),
                input_titulo,
                input_autor,
                input_isbn,
                ft.Divider(height=10),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            content=ft.Row([ft.Icon("save", size=16), ft.Text("Registrar libro")]),
                            on_click=ejecutar_guardado, height=40
                        ),
                        ft.OutlinedButton(
                            content=ft.Row([ft.Icon("arrow_back", size=16), ft.Text("Regresar")]),
                            on_click=lambda _: self.mostrar_vista_inicio(), height=40
                        )
                    ],
                    spacing=15
                ),
                text_mensaje
            ],
            spacing=15
        )
        self.page.update()

    def mostrar_menu_usuarios(self):
        self.area_contenido.content = ft.Column(
            controls=[
                ft.Text("Gestión de Usuarios", size=26, weight="bold", color="#4A4A4A"),
                ft.ElevatedButton("Ver lista de usuarios desde pgAdmin", on_click=lambda _: print("Cargando usuarios..."))
            ]
        )
        self.page.update()