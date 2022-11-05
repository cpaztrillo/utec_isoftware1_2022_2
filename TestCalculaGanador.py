import unittest
from CalculaGanador import *

# crear 6 casos de prueba adicionales que caigan en diferentes clases de datos de entrada
class TestStringMethods(unittest.TestCase):
    def test_ganador(self):
        datatest = [ ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'] ]
        c = CalculaGanador()
        self.assertEqual(c.calcularganador(datatest), ['Eddie Hinesley'])

    def test_ganadorvotoinvalido(self):
        datatest = [ ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
        ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1']]
        c = CalculaGanador()
        self.assertEqual(c.calcularganador(datatest), ['Aundrea Grace'])

if __name__ == '__main__':
    unittest.main()
