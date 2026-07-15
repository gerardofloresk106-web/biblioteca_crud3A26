# import flet as ft

# def libro_form():
#     titulo_input = ft.TextField(label="Título del libro:", width=400)
#     autor_input = ft.TextField(label="Autor:", width=400)
#     isbn_input = ft.TextField(label="ISBN:", width=400)


#     mensaje = ft.Text("", color=ft.Colors.GREEN)



#     titulo = ft.Text("Formulario de Libros", size=24, weight="bold", color=ft.Colors.BLUE_GREY_900)
#     subtitulo = ft.Text("Ingrese los detalles del libro", size=16, color=ft.Colors.BLUE_GREY_600)

#     contenido = ft.Container(
#         content=ft.Column(
#             controls=[
#                 titulo,
#                 subtitulo,
#                 # Aquí puedes agregar más controles para el formulario de libros
#             ],
#             spacing=10,
#         ),
#         padding=30,
#         expand=True
#     )

#     page.add(contenido)

import flet as ft
from dao.libro_dao import LibroDAO # Importamos tu nuevo DAO

class LibroForm:
    def __init__(self, page: ft.Page, ventana_principal):
        self.page = page
        self.ventana_principal = ventana_principal
        self.contenedor_formulario = ft.Container()

    def inicializar_formulario(self):
        self.mostrar_vista_registro()
        return self.contenedor_formulario

    def mostrar_vista_registro(self):
        input_titulo = ft.TextField(label="Título del Libro", width=400)
        input_id_autor = ft.TextField(label="ID Numérico del Autor (Llave Foránea)", width=400)
        text_mensaje = ft.Text("")

        def procesar_guardado(e):
            if not input_titulo.value or not input_id_autor.value:
                text_mensaje.value = "Por favor, llena todos los campos."
                text_mensaje.color = ft.colors.ORANGE_ACCENT
                self.page.update()
                return

            try:
                # Ejecutamos el método del DAO convirtiendo el ID de autor a entero
                LibroDAO.insertar(
                    titulo=input_titulo.value,
                    id_autor=int(input_id_autor.value)
                )
                
                text_mensaje.value = f"¡Libro '{input_titulo.value}' guardado con éxito en pgAdmin!"
                text_mensaje.color = ft.colors.GREEN_ACCENT
                input_titulo.value = ""
                input_id_autor.value = ""
            except Exception as ex:
                text_mensaje.value = f"Error en la base de datos: {ex}"
                text_mensaje.color = ft.colors.RED_ACCENT
            
            self.page.update()

        self.contenedor_formulario.content = ft.Column(
            controls=[
                ft.Text("====== REGISTRO DE NUEVO LIBRO ======", size=20, weight="bold"),
                ft.VerticalDivider(height=10),
                input_titulo,
                input_id_autor,
                ft.VerticalDivider(height=10),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Guardar Libro", on_click=procesar_guardado, bgcolor=ft.colors.BLUE_700, color="white"),
                        ft.OutlinedButton("Cancelar", on_click=lambda _: self.ventana_principal.mostrar_menu_administrador())
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
                text_mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
        self.page.update()