import flet as ft
from .base_view import BaseView
import auth


class PinRecoveryView(BaseView):
    def __init__(self, router):
        super().__init__(router, page_title="Recuperar PIN")

    def handle_recovery_click(self, e):
        """Handles the PIN recovery process."""
        list_users = auth.load_database()
        username = self.campo_usuario.value
        try:
            dni = int(self.campo_dni.value)
        except (ValueError, TypeError):
            self.resultado.value = "Error: El DNI debe ser un número válido."
            self.resultado.color = "red"
            self.resultado.update()
            return
        new_pin = self.campo_pin.value

        if auth.reset_pin(list_users, username, dni, new_pin):
            auth.save_database(list_users)
            self.resultado.value = "PIN actualizado con éxito."
            self.resultado.color = "green"
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("PIN actualizado. Ahora puede iniciar sesión."),
                bgcolor="green",
            )
            self.page.snack_bar.open = True
            self.router.change_route("/login")
        else:
            self.resultado.value = "Usuario o DNI incorrectos."
            self.resultado.color = "red"

        self.resultado.update()
        self.page.update()

    def handle_back_click(self, e):
        """Navigates back to the login view."""
        self.router.change_route("/login")

    def initialize_controls(self):
        """Creates and adds widgets for the PIN recovery view."""
        titulo_principal = ft.Text(
            "Recuperar PIN",
            size=30,
            weight=ft.FontWeight.BOLD,
            italic=True,
            color="blue",
        )
        self.campo_usuario = ft.TextField(label="Usuario", autofocus=True, width=300)
        self.campo_dni = ft.TextField(label="DNI", width=300)
        self.campo_pin = ft.TextField(
            label="Nuevo PIN", password=True, can_reveal_password=True, width=300
        )
        boton_recuperar = ft.ElevatedButton(
            "Recuperar PIN",
            on_click=self.handle_recovery_click,
            width=300,
            height=40,
        )
        boton_volver = ft.TextButton(
            "Volver al Login",
            on_click=self.handle_back_click,
            width=300,
            height=40,
        )
        self.resultado = ft.Text(value="", weight=ft.FontWeight.BOLD)

        self.controls = [
            titulo_principal,
            self.campo_usuario,
            self.campo_dni,
            self.campo_pin,
            boton_recuperar,
            boton_volver,
            self.resultado,
        ]
