import flet as ft
from .base_view import BaseView, auth


class UserPanelView(BaseView):
    def __init__(self, router):
        # This view requires authentication
        super().__init__(
            router, page_title=f"Panel de {router.user_data['username']}", needs_auth=True
        )

    def handle_logout(self, e):
        """Limpia los datos del usuario y vuelve a la pantalla de login."""
        self.router.user_data = None
        self.router.change_route("/login")

    def handle_deposit(self, e):
        """Navega a la vista de depósito."""
        self.router.change_route("/deposit")

    def handle_withdraw(self, e):
        """Navega a la vista de retiro."""
        self.router.change_route("/withdraw")

    def initialize_controls(self):
        """Construye la interfaz de usuario para el panel."""

        welcome_text = ft.Text(
            f"¡Bienvenido, {self.user['username']}!",
            size=24,
            weight=ft.FontWeight.BOLD,
        )
        account_info = ft.Text(f"Cuenta N°: {self.user['n_account']}", size=16)
        
        # We need to re-format the balance here in case it was updated
        balance_str = auth.format_balance(self.user["saldo"])
        balance_info = ft.Text(
            f"Saldo: {balance_str}", size=20, weight=ft.FontWeight.BOLD
        )

        deposit_button = ft.ElevatedButton(
            "Depositar",
            width=300,
            on_click=self.handle_deposit,
            icon=ft.Icons.ADD,
        )
        withdraw_button = ft.ElevatedButton(
            "Retirar",
            width=300,
            on_click=self.handle_withdraw,
            icon=ft.Icons.REMOVE,
        )
        logout_button = ft.ElevatedButton(
            "Cerrar Sesión",
            on_click=self.handle_logout,
            width=300,
            bgcolor=ft.Colors.RED_700,
            color=ft.Colors.WHITE,
        )

        self.controls = [
            welcome_text,
            account_info,
            balance_info,
            ft.Divider(),
            deposit_button,
            withdraw_button,
            ft.Divider(),
            logout_button,
        ]

