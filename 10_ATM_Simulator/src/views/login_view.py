import flet as ft
from .base_view import BaseView
import auth


class LoginView(BaseView):
    def __init__(self, router):
        # Call BaseView constructor, no auth needed
        super().__init__(router, page_title="ATM Simulator")

    def handle_login_click(self, e):
        """Función que se ejecuta al presionar el botón de login."""
        list_users = auth.load_database()
        username = self.campo_usuario.value
        pin = self.campo_pin.value

        user = auth.get_user_by_username(list_users, username)

        if user and user.get("failed_attempts", 0) >= 3:
            self.resultado.value = "CUENTA BLOQUEADA. Recupere su PIN."
            self.resultado.color = "red"
            self.resultado.update()
            return

        if user and auth.check_pin(user, pin):
            # Reset failed attempts on successful login
            if user.get("failed_attempts", 0) > 0:
                user["failed_attempts"] = 0
                auth.save_database(list_users)

            # Navigate to the user panel, passing user data
            self.router.change_route("/panel", data=user)
        else:
            # Handle failed login attempt
            if user:
                attempts = user.get("failed_attempts", 0) + 1
                user["failed_attempts"] = attempts
                auth.save_database(list_users)
                if attempts >= 3:
                    self.resultado.value = "CUENTA BLOQUEADA. Recupere su PIN."
                else:
                    self.resultado.value = f"PIN incorrecto. Intento {attempts}/3."
            else:
                self.resultado.value = "Usuario o PIN incorrecto."

            self.resultado.color = "red"
            self.resultado.update()

    def handle_register_click(self, e):
        """Navigates to the register view."""
        self.router.change_route("/register")

    def handle_recovery_click(self, e):
        """Navigates to the recovery view."""
        self.router.change_route("/recovery")

    def initialize_controls(self):
        """Creates and adds widgets for the login view."""
        titulo_principal = ft.Text(
            "ATM Simulator",
            size=30,
            weight=ft.FontWeight.BOLD,
            italic=True,
            color="blue",
        )
        self.campo_usuario = ft.TextField(label="Usuario", autofocus=True, width=300)
        self.campo_pin = ft.TextField(
            label="PIN", password=True, can_reveal_password=True, width=300
        )
        boton_login = ft.ElevatedButton(
            "Iniciar Sesión",
            on_click=self.handle_login_click,
            width=300,
            height=40,
        )
        boton_register = ft.TextButton(
            "Registrarse",
            on_click=self.handle_register_click,
            width=300,
            height=40,
        )
        boton_recovery = ft.TextButton(
            "Recuperar PIN",
            on_click=self.handle_recovery_click,
            width=300,
            height=40,
        )
        self.resultado = ft.Text(value="", weight=ft.FontWeight.BOLD)

        self.controls = [
            titulo_principal,
            self.campo_usuario,
            self.campo_pin,
            boton_login,
            ft.Row(
                controls=[
                    boton_register,
                    boton_recovery,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            self.resultado,
        ]
