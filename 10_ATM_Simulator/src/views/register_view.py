import flet as ft
import random
from .base_view import BaseView, auth


class RegisterView(BaseView):
    def __init__(self, router):
        super().__init__(router, page_title="Registrarse")

    def handle_register_click(self, e):
        # 1. Cargar la base de datos en una variable
        list_users = auth.load_database()

        # 2. Obtener valores de los campos
        username = self.campo_usuario.value
        pin = self.campo_pin.value

        # 3. Validar y convertir DNI a número
        try:
            dni = int(self.campo_dni.value)
        except (ValueError, TypeError):
            self.resultado.value = "Error: El DNI debe ser un número válido."
            self.resultado.color = "red"
            self.resultado.update()
            return

        # 4. Verificar si el usuario ya existe ANTES de registrar
        if auth.verify_user(list_users, username, dni):
            self.resultado.value = "Error: El usuario o DNI ya están registrados."
            self.resultado.color = "red"
        else:
            # 5. Si no existe, proceder con el registro
            n_account = random.randint(100000, 999999)
            saldo_inicial = 0

            auth.register_user(list_users, username, dni, pin, n_account, saldo_inicial)
            auth.save_database(list_users)  # ¡Importante! Guardar en el archivo

            self.resultado.value = f"¡Usuario '{username}' registrado con éxito!"
            self.resultado.color = "green"
            # Después de un registro exitoso, volver al login
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Registro exitoso. Ahora puede iniciar sesión."),
                bgcolor="green",
            )
            self.page.snack_bar.open = True
            self.router.change_route("/login")

        self.resultado.update()

    def initialize_controls(self):
        """Creación y agregado de widgets."""
        titulo_principal = ft.Text(
            "Registrarse", size=30, weight=ft.FontWeight.BOLD, italic=True, color="blue"
        )

        self.campo_usuario = ft.TextField(label="Usuario", autofocus=True, width=300)
        self.campo_dni = ft.TextField(label="DNI", width=300)
        self.campo_pin = ft.TextField(
            label="PIN", password=True, can_reveal_password=True, width=300
        )

        boton_register = ft.ElevatedButton(
            "Registrarse",
            on_click=self.handle_register_click,
            width=300,
            height=40,
        )

        boton_volver = ft.TextButton(
            "Volver al Login", on_click=lambda _: self.router.change_route("/login")
        )

        self.resultado = ft.Text(value="", weight=ft.FontWeight.BOLD)

        self.controls = [
            titulo_principal,
            self.campo_usuario,
            self.campo_dni,
            self.campo_pin,
            boton_register,
            self.resultado,
            boton_volver,
        ]
