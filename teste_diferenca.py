import unittest
from diferenca import diferenca

class TestDiferenca(unittest.TestCase):
    def test_diferenca(self):
        #Testa se encontrou corretamente a diferenca
        self.assertAlmostEqual(diferenca([-2,-5,0,5,55,46,7, 12], 5), 3)
        self.assertAlmostEqual(diferenca([1,5,3,4,2], 2), 3)

    def test_valor_argumento_diferenca(self):
        #Garante que lançará exceção se o array estiver vazio ou se 'dif' for negativo
        self.assertRaises(ValueError, diferenca, [], 1)
        self.assertRaises(ValueError, diferenca, [10,20,30], -10)

    def test_tipo_argumento_diferenca(self):
        #Garante que lançará exceção se o array de entrada tiver elementos não númericos
        self.assertRaises(TypeError, diferenca, [True, 3, 2], 1)
        self.assertRaises(TypeError, diferenca, [1, 2, 3], 'a')