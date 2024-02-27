import unittest
from fracao import Fracao

class FracaoTeste (unittest.TestCase):
    def test_Fracao_ok(self):
        f = Fracao(1, 2)

        self.assertEqual(1, f.numerador)
        self.assertEqual(2, f.denominador)

    def test_Fracao_type_error_numerador(self):
        with self.assertRaises(TypeError):
            Fracao('1', 2)
    
    def test_Fracao_type_error_denominador(self):
        with self.assertRaises(TypeError):
            Fracao(1, '2')

    def test_Fracao_denominador_zero(self):
        with self.assertRaises(ValueError):
            Fracao(1, 0)

    def test_multiplicar(self):
        f1 = Fracao(1, 2)
        f2 = Fracao(3, 5)
        resultado = f1.multiplicar(f2)

        self.assertEqual(3, resultado.numerador)
        self.assertEqual(10, resultado.denominador)

    def test_dividir(self):
        f1 = Fracao(1, 2)
        f2 = Fracao(3, 5)
        resultado = f1.dividir(f2)

        self.assertEqual(5, resultado.numerador)
        self.assertEqual(6, resultado.denominador)

if __name__ == "__main__":
    unittest.main()