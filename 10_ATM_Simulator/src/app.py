import flet as ft
from views.router import Router


def main(page: ft.Page):
    """
    Función principal que inicializa la aplicación Flet y el enrutador.
    """
    # Configuraciones globales de la página
    page.title = "ATM Simulator"
    page.theme_mode = ft.ThemeMode.DARK

    # Inicializa el enrutador que gestionará las vistas
    Router(page)


ft.app(main)
