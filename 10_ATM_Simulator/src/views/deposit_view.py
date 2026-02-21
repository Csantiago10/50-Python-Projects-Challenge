import flet as ft
from .base_view import BaseView, operations, auth


class DepositView(BaseView):
    def __init__(self, router):
        super().__init__(router, page_title="Depositar Fondos", needs_auth=True)

    def handle_deposit_click(self, e):
        try:
            amount = int(self.campo_monto.value)
            if amount <= 0:
                self.resultado.value = "Error: El monto debe ser positivo."
                self.resultado.color = "red"
                self.resultado.update()
                return
        except (ValueError, TypeError):
            self.resultado.value = "Error: Ingrese un monto numérico válido."
            self.resultado.color = "red"
            self.resultado.update()
            return

        success_msg = f"Depósito de {auth.format_balance(amount)} realizado con éxito."

        # Use the DRY method from BaseView
        self.update_user_data_and_navigate(operations.deposit_money, amount, success_msg)

    def initialize_controls(self):
        titulo = ft.Text("Depositar", size=24, weight=ft.FontWeight.BOLD)

        saldo_actual = ft.Text(f"Saldo Actual: {self.user['saldo_str']}", size=16)

        self.campo_monto = ft.TextField(
            label="Monto a depositar",
            autofocus=True,
            width=300,
            prefix_icon= ft.Icons.MONEY, 
            prefix=ft.Text("$"),
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        boton_depositar = ft.ElevatedButton(
            "Aceptar",
            on_click=self.handle_deposit_click,
            width=300,
            height=40,
            icon=ft.Icons.ADD,
        )

        boton_volver = ft.TextButton(
            "Volver",
            on_click=lambda _: self.router.change_route("/panel"),
            icon=ft.Icons.ARROW_BACK,
        )

        self.resultado = ft.Text(value="", weight=ft.FontWeight.BOLD)

        self.controls = [
            titulo,
            saldo_actual,
            self.campo_monto,
            boton_depositar,
            self.resultado,
            ft.Divider(),
            boton_volver,
        ]
