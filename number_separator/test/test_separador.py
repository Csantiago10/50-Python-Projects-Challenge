import unittest
import sys
import os

# Rutina estándar para encontrar la carpeta 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- CAMBIO IMPORTANTE 1: Importamos la NUEVA función ---
from src.separador_par_impar import obtener_listas_par_impar

class TestClasificador(unittest.TestCase):

    def test_clasificacion_completa(self):
        # 1. Datos de prueba (strings desordenados)
        entrada = ['10', '3', '2', '5', '8']
        
        # 2. Ejecutamos tu NUEVA función
        # Tu función retorna una lista con dos listas adentro: [[pares], [impares]]
        resultado = obtener_listas_par_impar(entrada)
        
        # Separamos el resultado para verificar
        pares_obtenidos = resultado[0]   # La primera lista son los pares
        impares_obtenidos = resultado[1] # La segunda son los impares
        
        # 3. Verificamos que estén ordenados y correctos
        self.assertEqual(pares_obtenidos, [2, 8, 10])
        self.assertEqual(impares_obtenidos, [3, 5])

    def test_con_datos_basura(self):
        # Probamos tu bloque try-except con una letra "A"
        entrada = ['2', 'A', '5']
        
        resultado = obtener_listas_par_impar(entrada)
        
        # Debería ignorar la "A" y procesar el resto
        self.assertEqual(resultado[0], [2]) # Pares
        self.assertEqual(resultado[1], [5]) # Impares

if __name__ == '__main__':
    unittest.main()