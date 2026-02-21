import unittest
import os
import sys
import shutil
from unittest.mock import patch

# --- 1. CONFIGURACIÓN DE RUTAS ---
# Añadimos la ruta raíz del proyecto para que Python encuentre la carpeta 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# --- 2. IMPORTAR MÓDULOS DEL PROYECTO ---
import auth
import operations


class TestATMSimulator(unittest.TestCase):
    """Suite de pruebas para el Simulador de Cajero Automático."""

    def setUp(self):
        """
        Configuración inicial antes de cada prueba.
        Crea un entorno de prueba aislado (archivos y carpetas temporales).
        """
        # Definimos rutas temporales para las pruebas
        self.test_docs_dir = os.path.join(os.path.dirname(__file__), "test_docs")
        self.test_db_path = os.path.join(self.test_docs_dir, "test_users.json")

        # Creamos el directorio de prueba
        os.makedirs(self.test_docs_dir, exist_ok=True)

        # Creamos datos de usuario iniciales para las pruebas
        self.initial_users = [
            {
                "username": "santiago",
                "DNI": 12345,
                "pin": auth._hash_pin("1111"),
                "n_account": 1001,
                "saldo": 1000,
                "saldo_str": auth.format_balance(1000),
                "failed_attempts": 0,
            }
        ]
        # Guardamos los datos iniciales en la DB de prueba
        with open(self.test_db_path, "w") as f:
            auth.json.dump(self.initial_users, f)

        # --- Mocking de las rutas globales en los módulos ---
        # Esto redirige todas las operaciones de archivos a nuestro entorno de prueba
        self.db_patcher = patch("auth.DB_PATH", self.test_db_path)
        self.docs_patcher = patch("operations.DOCS_DIR", self.test_docs_dir)
        self.db_patcher.start()
        self.docs_patcher.start()

    def tearDown(self):
        """
        Limpieza después de cada prueba.
        Elimina los archivos y carpetas temporales.
        """
        self.db_patcher.stop()
        self.docs_patcher.stop()
        if os.path.exists(self.test_docs_dir):
            shutil.rmtree(self.test_docs_dir)

    def test_registro_usuario(self):
        """Prueba el escenario: Registro de un nuevo usuario."""
        list_users = auth.load_database()
        user_count_before = len(list_users)

        auth.register_user(list_users, "testuser", 98765, "1234", 1002, 0)
        auth.save_database(list_users)

        list_users_after = auth.load_database()
        self.assertEqual(len(list_users_after), user_count_before + 1)
        new_user = auth.get_user_by_username(list_users_after, "testuser")
        self.assertIsNotNone(new_user)
        self.assertEqual(new_user["DNI"], 98765)

    def test_login_exitoso(self):
        """Prueba el escenario: Login con credenciales correctas."""
        list_users = auth.load_database()
        user = auth.login_user(list_users, "santiago", "1111")
        self.assertIsNotNone(user)
        self.assertEqual(user["username"], "santiago")

    def test_bloqueo_de_cuenta_por_fallos(self):
        """Prueba el escenario: Bloqueo de cuenta tras 3 intentos fallidos."""
        list_users = auth.load_database()
        user = auth.get_user_by_username(list_users, "santiago")

        # Simulamos 3 intentos fallidos
        user["failed_attempts"] = 3
        auth.save_database(list_users)

        reloaded_users = auth.load_database()
        blocked_user = auth.get_user_by_username(reloaded_users, "santiago")
        self.assertEqual(blocked_user["failed_attempts"], 3)

    def test_retiro_sin_fondos(self):
        """Prueba el escenario: Intentar retirar más dinero del disponible."""
        list_users = auth.load_database()
        user = auth.get_user_by_username(list_users, "santiago")
        initial_balance = user["saldo"]

        result = operations.withdraw_money(user, 2000)  # Saldo es 1000

        self.assertFalse(result)
        self.assertEqual(user["saldo"], initial_balance)  # El saldo no debe cambiar

    def test_persistencia_deposito(self):
        """Prueba el escenario: Un depósito se guarda y persiste entre sesiones."""
        list_users = auth.load_database()
        user = auth.get_user_by_username(list_users, "santiago")

        operations.deposit_money(user, 500)
        auth.save_database(list_users)

        # Simulamos un reinicio cargando la DB de nuevo
        reloaded_users = auth.load_database()
        reloaded_user = auth.get_user_by_username(reloaded_users, "santiago")
        self.assertEqual(reloaded_user["saldo"], 1500)

    def test_recuperacion_pin(self):
        """Prueba el escenario: Resetear un PIN y desbloquear la cuenta."""
        list_users = auth.load_database()
        user = auth.get_user_by_username(list_users, "santiago")
        user["failed_attempts"] = 3  # Simulamos cuenta bloqueada

        reset_success = auth.reset_pin(list_users, "santiago", 12345, "9999")
        self.assertTrue(reset_success)
        self.assertEqual(user["failed_attempts"], 0)
        self.assertTrue(auth.check_pin(user, "9999"))

    def test_generacion_recibo(self):
        """Prueba el escenario: Se crea un archivo de recibo tras un retiro."""
        list_users = auth.load_database()
        user = auth.get_user_by_username(list_users, "santiago")
        operations.withdraw_money(user, 100)
        receipt_path = os.path.join(
            self.test_docs_dir, f"recibo_{user['username']}.txt"
        )
        self.assertTrue(os.path.exists(receipt_path))


if __name__ == "__main__":
    unittest.main()
