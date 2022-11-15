import unittest
from CalculaGanador import *

# crear 6 casos de prueba adicionales que caigan en diferentes clases de datos de entrada
class TestStringMethods(unittest.TestCase):
    def test_ganador(self):
        datatest = [ ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'] ]
        c = CalculaGanador()
        self.assertEqual(c.calcularganador(datatest,0), ['Eddie Hinesley'])

    def test_ganadorvotoinvalido(self):
        datatest = [ ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
        ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1']]
        c = CalculaGanador()
        self.assertEqual(c.calcularganador(datatest,0), ['Aundrea Grace'])

    def test_ganadordniinvalido(self):
        datatest = [ ['Áncash', 'Asunción', 'Acochaca', '4081006', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1']]
        c = CalculaGanador()
        self.assertEqual(c.calcularganador(datatest,0), ['Aundrea Grace'])

    def test_segundavuelta(self):
        datatest = [ ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '40810072', 'Nhium Hai', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1']]
        c = CalculaGanador()
        self.assertEqual(c.calcularganador(datatest,0), ['Segunda Vuelta'])

if __name__ == '__main__':
    unittest.main()
