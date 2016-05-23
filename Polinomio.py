from Monomio import Monomio

class Polinomio:

    def __init__(self):
        self.monomios = []

    # @return Evalua y suma cada monomio en la lista.
    def evaluar(self, x, y):
        res = 0
        for m in self.monomios:
            if m.literal == 'x':
                res += m.evaluar(x)
            elif m.literal == 'y':
                res += m.evaluar(y)
            else:
                res += m.evaluar(1)

        return res
