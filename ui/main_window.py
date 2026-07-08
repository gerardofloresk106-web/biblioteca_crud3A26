import flet as ft

def main_window(page:ft.Page):
    page.title = "Sistema de Biblioteca Universitaria"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 0
    #page.bgcolor = "#f5f5f5"
    page.bgcolor = ft.colors.BLUE_GREY_50
#titulo y subtitulo de la ventana
    titulo = ft.Text("Sistema de Biblioteca Universitaria", size=24, weight=ft.FontWeight.BOLD)
#subtitulo de la ventana
    subtitulo = ft.Text("Bienvenido al sistema de gestión de biblioteca", size=16 color=ft.colors.BLUE_GREY_600)
#widget container para contener el contenido de la ventana
    contenido = ft.Container(
    content = ft.Column(
        controls = [
            titulo,
            subtitulo
            ],
            spacing = 10,
    ),
    padding = 30,
    expand = True

    )

    menu_lateral = ft.container(
        width = 220,
        bgcolor = ft.colors.BLUE_GREY_900,
        padding = 20,
        content = ft.Column(
            controls = [
                ft.Text("Biblioteca", size=20, weight=ft.FontWeight.BOLD),
                
            ]
        )
    )