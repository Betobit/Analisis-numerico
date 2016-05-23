from Polinomio import Polinomio

class Integracion:

    def __init__(self, polinomio):
        self.polinomio = polinomio

    def trapecio(self, a, b):
        fa = self.polinomio.evaluar(a, 0)
        fb = self.polinomio.evaluar(b, 0)

        return (b-a) * (fa +fb) / 2

    def simpsonUnTercio(self, a, b):
        h = (b - a) / 2
        f1 = self.polinomio.evaluar(a, 0)
        f2 = self.polinomio.evaluar(a+h, 0) * 4
        f3 = self.polinomio.evaluar(b, 0)

        return h / 3 * (f1 + f2 + f3)

    def simpsonTresOctavos(self, a, b):
        h = (b - a) / 3
        f1 = self.polinomio.evaluar(a, 0)
        f2 = self.polinomio.evaluar((2 * a + b) / 3, 0) * 3
        f3 = self.polinomio.evaluar((a + 2 * b) / 3, 0) * 3
        f4 = self.polinomio.evaluar(b, 0)

        return 3 * h / 8 * (f1 + f2 + f3 + f4)
