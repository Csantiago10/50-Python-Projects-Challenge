import unittest
import string
import sys
import os

# TRUCO DE INGENIERO: 
# Esto ayuda a Python a encontrar tu carpeta 'src' aunque estés en otra carpeta.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import generador

class TestGeneradorPassword(unittest.TestCase):

    # --- PRUEBA 1: Verificar la Longitud ---
    def test_longitud_exacta(self):
        """El generador debe respetar estrictamente la longitud pedida"""
        config = {
            'longitud': 12,
            'pool': string.ascii_lowercase # Solo minúsculas para probar
        }
        resultado = generador.generar_password(config)
        
        # ASERCIÓN: Si esto no es igual, la prueba falla (Rojo)
        self.assertEqual(len(resultado), 12)

    # --- PRUEBA 2: Construcción del Pool (Ingredientes) ---
    def test_pool_solo_numeros(self):
        """Si pido números, el pool debe contener dígitos"""
        # Asumiendo que tienes una función para construir el pool
        # Si tu función se llama diferente, cambia 'construir_pool' aquí
        pool_generado = generador.construir_pool(minis="N", mayus="N", nums="S", simb="N")
        
        # Verificamos que '1' esté en el pool y 'a' esté en el pool (base)
        self.assertIn('1', pool_generado)
        self.assertIn('a', pool_generado)
        # Verificamos que NO tenga símbolos
        self.assertNotIn('@', pool_generado)

    # --- PRUEBA 3: Robustez (Pool Vacío o Error) ---
    def test_longitud_cero(self):
        """Generar una contraseña de longitud 0 debe devolver string vacío"""
        config = {
            'longitud': 0,
            'pool': string.ascii_lowercase
        }
        resultado = generador.generar_password(config)
        self.assertEqual(resultado, "")

if __name__ == '__main__':
    unittest.main()