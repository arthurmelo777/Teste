class Fracao:
    def __init__ (self, n, d):
        if (not isinstance(n, int)) or (not isinstance(d, int)):
            raise TypeError('Parametros devem ser do tipo inteiro')
        if d == 0:
            raise ValueError('Denominador deve ser diferente de zero')
        self._numerador = n
        self._denominador = d

    @property
    def numerador(self):
        return self._numerador
    
    @property
    def denominador(self):
        return self._denominador

    def multiplicar(self, f):
        n = self.numerador * f.numerador
        d = self.denominador * f.denominador
        return Fracao(n, d)
    
    def dividir(self, f):
        n = self.numerador * f.denominador
        d = self.denominador * f.numerador
        return Fracao(n, d)