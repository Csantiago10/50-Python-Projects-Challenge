import unittest
import sys
import os

# --- 1. CONFIGURACIÓN DE RUTAS ---
# Esto permite que Python encuentre la carpeta 'src' aunque estemos en 'test'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- 2. IMPORTAR TUS FUNCIONES ---
# Asegúrate de que tu archivo de lógica se llame 'conversiones.py' dentro de 'src'
from src.conversor_universal import (
    km_to_miles, miles_to_km, celsius_to_fahrenheit, fahrenheit_to_celsius, kg_to_pounds, pounds_to_kg        
)

class TestConversiones(unittest.TestCase):
    
    # --- PRUEBAS DE LONGITUD ---
    def test_km_a_millas(self):
        # 10 Km deberían ser aprox 6.21 millas
        resultado = km_to_miles(10)
        # Usamos assertAlmostEqual para decimales (por si da 6.21371...)
        self.assertAlmostEqual(resultado, 6.21371, places=2)

    def test_millas_a_km(self):
        # 10 Millas deberían ser aprox 16.09 km
        resultado = miles_to_km(10)
        self.assertAlmostEqual(resultado, 16.0934, places=2)

    # --- PRUEBAS DE TEMPERATURA ---
    def test_celsius_a_fahrenheit(self):
        # 0°C (congelación) debe ser 32°F
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        # 100°C (ebullición) debe ser 212°F
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_a_celsius(self):
        # 32°F debe ser 0°C
        self.assertEqual(fahrenheit_to_celsius(32), 0)

    # --- PRUEBAS DE MASA ---
    def test_kg_a_libras(self):
        # 1 Kg es aprox 2.20462 Libras
        resultado = kg_to_pounds(1)
        self.assertAlmostEqual(resultado, 2.20462, places=3)

    def test_libras_a_kg(self):
        # 1 Libra es aprox 0.453592 Kg
        resultado = pounds_to_kg(1)
        self.assertAlmostEqual(resultado, 0.453592, places=3)

if __name__ == '__main__':
    unittest.main()