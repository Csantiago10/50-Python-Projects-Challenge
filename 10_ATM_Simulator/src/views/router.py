import flet as ft

# Importaciones relativas ya que estamos dentro del mismo paquete 'views'
from .login_view import LoginView
from .register_view import RegisterView
from .user_panel_view import UserPanelView
from .deposit_view import DepositView
from .cashier_view import CashierView
from .pin_recovery_view import PinRecoveryView


class Router:
    """
    Clase central para gestionar la navegación y el estado entre vistas.
    """

    def __init__(self, page: ft.Page):
        self.page = page
        self.user_data = None  # Almacenará los datos del usuario logueado

        # Diccionario que mapea rutas a las clases de las vistas
        self.routes = {
            "/login": LoginView,
            "/register": RegisterView,
            "/panel": UserPanelView,
            "/deposit": DepositView,
            "/withdraw": CashierView,
            "/recovery": PinRecoveryView,
        }

        # Contenedor principal donde se renderizará la vista actual
        self.body = ft.Container()
        self.page.add(self.body)

        # Iniciar en la ruta de login
        self.change_route("/login")

    def change_route(self, route_path: str, data=None):
        """
        Cambia la vista actual renderizando la nueva ruta.
        """
        # Almacena datos si se pasan (ej. datos del usuario al hacer login)
        if data:
            self.user_data = data

        # Renderiza la nueva vista pasándose a sí mismo (el router)
        # Asegurarse de que la ruta exista para evitar errores
        if route_path in self.routes:
            self.body.content = self.routes[route_path](self)
            self.page.update()
        else:
            print(f"Error: La ruta '{route_path}' no fue encontrada.")

