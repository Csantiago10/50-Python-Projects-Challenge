import unittest
import sys
import os

# Rutina estándar para encontrar la carpeta 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- CAMBIO IMPORTANTE 1: Importamos la NUEVA función ---
from src.words_counter import word_counter, frequency_counter

class TestWordCounter(unittest.TestCase):
    """
    Tests for word_counter and frequency_counter"""
    def test_basico(self):
        """Scenary: 'Hola mundo' -> Total: 2"""
        texto = "Hola mundo"
        # Tested the counts
        self.assertEqual(word_counter(texto), 2)

    def test_normalizacion(self):
        """ScenarY: 'Hola, hola.' -> Total: 'hola' dos veces"""
        texto = "Hola, hola."
        frecuencias = frequency_counter(texto)
        # Tested the counts of 'hola' in the dictionary
        self.assertEqual(frecuencias.get("hola"), 2)

    def test_texto_vacio(self):
        """scenary: text empty -> Total: 0"""
        self.assertEqual(word_counter(""), 0)

    def test_ranking(self):
        """Scenary: 'a a a b b c' -> Top: [('a', 3), ('b', 2), ('c', 1)]"""
        texto = "a a a b b c"
        frecuencias = frequency_counter(texto)
        self.assertEqual(frecuencias["a"], 3)
        self.assertEqual(frecuencias["b"], 2)
        self.assertEqual(frecuencias["c"], 1)

if __name__ == "__main__":
    unittest.main()