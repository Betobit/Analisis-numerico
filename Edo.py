from Polinomio import Polinomio

# Ecuación diferencial ordinaria
class Edo:

    def __init__(self, polinomio, h):
        self.polinomio = polinomio
        self.h = h

    def euler(self, x, y):
        r = self.polinomio.evaluar(x, y)
        #print(r)
        return r * self.h + y

    def rungeKutta(self, x, y):
        k0 = self.polinomio.evaluar(x, y)
        k1 = self.polinomio.evaluar(self.h + x, y + self.h * k0)

        return y + self.h / 2 * (k0 + k1)
