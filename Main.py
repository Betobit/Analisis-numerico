from Monomio import Monomio
from Polinomio import Polinomio
from Edo import Edo

# f'(x) = y - t^2 + 1
polinomio = Polinomio()
polinomio.monomios.append(Monomio(1, 'y', 1))
polinomio.monomios.append(Monomio(-1, 'x', 2))
polinomio.monomios.append(Monomio(1, '', 1))

# Intervalo a calcular
x1 = 0
x2 = 2
y = 1.5
h = 0.2
edo = Edo(polinomio, h)

i = 0
while x1 <= x2:
    print('{0}, {1}, {2}, {3}'.format(i, x1, y, edo.rungeKutta4(x1, y)))
    y = edo.rungeKutta4(x1, y)
    x1 += h
    i += 1
