# test_calculadora.py

import unittest
from calculadora import suma, resta, multiplicacion, division # Importa las funciones a probar

class TestCalculadora(unittest.TestCase):
    """Clase de pruebas unitarias para la calculadora."""

    def test_suma(self):
        """Prueba la función de suma."""
        self.assertEqual(suma(5, 3), 8, "Debería ser 8")
        self.assertEqual(suma(-1, 1), 0, "Debería ser 0")
        self.assertEqual(suma(-1, -1), -2, "Debería ser -2")

    def test_resta(self):
        """Prueba la función de resta."""
        self.assertEqual(resta(10, 4), 6, "Debería ser 6")
        self.assertEqual(resta(5, 5), 0, "Debería ser 0")
        self.assertEqual(resta(0, 5), -5, "Debería ser -5")

    def test_multiplicacion(self):
        """Prueba la función de multiplicación."""
        self.assertEqual(multiplicacion(2, 3), 6, "Debería ser 6")
        self.assertEqual(multiplicacion(5, 0), 0, "Debería ser 0")
        self.assertEqual(multiplicacion(-2, 4), -8, "Debería ser -8")

    def test_division(self):
        """Prueba la función de división, incluyendo el caso de error."""
        self.assertEqual(division(10, 2), 5.0, "Debería ser 5.0")
        self.assertEqual(division(1, 3), 1/3, "Debería ser 0.333...")
        # Prueba la división por cero
        self.assertEqual(division(5, 0), "Error: División por cero", "Debería retornar el mensaje de error")

# El resto del archivo calculadora.py (el código que pide input) 
# puede causar problemas al ejecutar las pruebas automatizadas.
# Para evitarlo, se recomienda añadir este bloque al final de tu archivo original:

# if __name__ == '__main__':
#     # Aquí va todo el código de 'print' e 'input' de tu calculadora
#     pass # O puedes dejarlo fuera de esta condición si ya está en otro script.