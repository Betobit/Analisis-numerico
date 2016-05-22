from Monomio import Monomio
from Polinomio import Polinomio
from Edo import Edo

# f'(x) = -2y
polinomio = Polinomio()
polinomio.monomios.append(Monomio(-2, 'y', 1))

# Intervalo a calcular
x1 = 0
x2 = 2
y = 1
h = 0.25
edo = Edo(polinomio, h)

i = 0
while x1 <= x2:
    print('{0}, {1}, {2}, {3}'.format(i, x1, y, edo.rungeKutta(x1, y)))
    y = edo.rungeKutta(x1, y)
    x1 += h
    i += 1
