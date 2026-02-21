import flet as ft
from .base_view import BaseView, operations, auth


class CashierView(BaseView):
    def __init__(self, router):
        super().__init__(router, page_title="Retirar Fondos", needs_auth=True)

    def handle_withdraw_click(self, e):
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

        # UI-level check for better UX, even though the backend validates it too
        if amount > self.user["saldo"]:
            self.resultado.value = "Error: Fondos insuficientes."
            self.resultado.color = "red"
            self.resultado.update()
            return

        success_msg = f"Retiro de {auth.format_balance(amount)} realizado con éxito."

        # Use the DRY method from BaseView
        self.update_user_data_and_navigate(
            operations.withdraw_money, amount, success_msg
        )

    def initialize_controls(self):
        titulo = ft.Text("Retirar", size=24, weight=ft.FontWeight.BOLD)

        saldo_actual = ft.Text(f"Saldo Actual: {self.user['saldo_str']}", size=16)

        self.campo_monto = ft.TextField(
            label="Monto a retirar",
            autofocus=True,
            width=300,
            prefix=ft.Text("$"),
            keyboard_type=ft.KeyboardType.NUMBER,
        )

        boton_retirar = ft.ElevatedButton(
            "Aceptar",
            on_click=self.handle_withdraw_click,
            width=300,
            height=40,
            icon=ft.Icons.REMOVE,
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
            boton_retirar,
            self.resultado,
            ft.Divider(),
            boton_volver,
        ]
