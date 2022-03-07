import unittest
from mediana import mediana

class TestMediana(unittest.TestCase):
    def test_mediana(self):
        #Testa se encontrou corretamente a mediana
        self.assertAlmostEqual(mediana([10 ,5, 15, 64, 2 ,879, 7, 0, 2]), 7)
        self.assertAlmostEqual(mediana([1, 2, 3]), 2)
        self.assertAlmostEqual(mediana([9,2,1,4,6]), 4)
        self.assertAlmostEqual(mediana([-11, -32, 10, 1112, 0]), 0)

    def test_valor_argumento_mediana(self):
        #Garante que lançará exceção se o array de entrada não tiver quantidade ímpar de elmentos ou se estiver vazio
        self.assertRaises(ValueError, mediana, [1, 2])
        self.assertRaises(ValueError, mediana, [])

    def test_tipo_argumento_mediana(self):
        #Garante que lançará exceção se o array de entrada tiver elementos não númericos
        self.assertRaises(TypeError, mediana, [True, 3, 2])
        self.assertRaises(TypeError, mediana, [1, '3', None])