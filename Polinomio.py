from Monomio import Monomio

class Polinomio:

    monomios = []

    # @return Evalua y suma cada monomio en la lista.
    def evaluar(self, x, y):
        res = 0
        for m in self.monomios:
            if m.literal == 'x':
                res += m.evaluar(x)
            else:
                res += m.evaluar(y)

        return res
