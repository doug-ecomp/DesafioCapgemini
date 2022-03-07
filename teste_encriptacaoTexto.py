import unittest
from encriptacaoTexto import encriptacaoTexto

class TestencriptacaoTexto(unittest.TestCase):
    def test_encriptacaoTexto(self):
        #Testa se encontrou corretamente a encriptacaoTexto
        self.assertEqual(encriptacaoTexto('ola mundo'), 'omd luo an')
        self.assertEqual(encriptacaoTexto('tenha um bom dia'), 'taoa eum nmd hbi')
        self.assertEqual(encriptacaoTexto('eu sou douglas'), 'eool uuua sdgs')

    def test_valor_argumento_encriptacaoTexto(self):
        #Garante que lançará exceção se o texto de entrada for uma string vazia
        self.assertRaises(ValueError, encriptacaoTexto, '')

    def test_tipo_argumento_encriptacaoTexto(self):
        #Garante que lançará exceção se o texto não for do tipo 'str'
        self.assertRaises(TypeError, encriptacaoTexto, True)
        self.assertRaises(TypeError, encriptacaoTexto, 1)
        self.assertRaises(TypeError, encriptacaoTexto, [1])