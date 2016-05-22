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

    def rungeKutta2(self, x, y):
        k0 = self.polinomio.evaluar(x, y)
        k1 = self.polinomio.evaluar(self.h + x, y + self.h * k0)

        return y + self.h / 2 * (k0 + k1)

    def rungeKutta4(self, x, y):
        k0 = self.polinomio.evaluar(x, y)
        k1 = self.polinomio.evaluar(x + self.h / 2, y + self.h * k0 /2)
        k2 = self.polinomio.evaluar(x + self.h / 2, y + self.h * k1 /2)
        k3 = self.polinomio.evaluar(x + self.h, y + self.h * k2)

        return y + self.h / 6 * (k0 + 2 * k1 + 2 * k2 + k3)
