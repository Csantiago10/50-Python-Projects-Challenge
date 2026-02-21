import flet as ft
import os
import sys

# Fix the path once for all views that will import this base class
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import auth
import operations


class BaseView(ft.Column):
    def __init__(self, router, page_title: str, needs_auth: bool = False):
        """
        Constructor for the base view.
        :param router: The application router instance.
        :param page_title: The title to set for the page.
        :param needs_auth: Boolean indicating if the view requires an authenticated user.
        """
        super().__init__()
        self.router = router
        self.user = router.user_data

        # --- Centralized Page and View Configuration ---
        self.router.page.title = page_title
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 20
        self.router.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.router.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.router.page.window_width = 400
        self.router.page.window_height = 550  # A bit taller for more content

        # --- Centralized Authentication Check ---
        if needs_auth and not self.user:
            # If auth is needed and there's no user, redirect to login and stop processing.
            self.router.change_route("/login")
            return

        # Let the subclass build its specific controls
        self.initialize_controls()

    def initialize_controls(self):
        """
        Subclasses must implement this method to build their UI.
        This is where widgets are created and added to `self.controls`.
        """
        raise NotImplementedError("Subclasses must implement initialize_controls()")

    def update_user_data_and_navigate(
        self, operation_func, amount: int, success_message: str
    ):
        """
        DRY method to handle deposit and withdraw logic.
        Loads DB, finds user, performs operation, saves DB, updates router state, and navigates.
        """
        list_users = auth.load_database()
        user_from_db = auth.get_user_by_username(list_users, self.user["username"])

        if user_from_db:
            result = operation_func(user_from_db, amount)
            if result:
                auth.save_database(list_users)
                self.router.user_data = user_from_db  # Update state in router

                self.router.page.snack_bar = ft.SnackBar(
                    content=ft.Text(success_message), bgcolor="green"
                )
                self.router.page.snack_bar.open = True
                self.router.change_route("/panel")
            else:
                # This could happen if withdraw_money fails due to insufficient funds (server-side check)
                self.resultado.value = "Error: Fondos insuficientes o monto inválido."
                self.resultado.color = "red"
                self.resultado.update()
        else:
            self.resultado.value = "Error: no se pudo encontrar el usuario."
            self.resultado.color = "red"
            self.resultado.update()
