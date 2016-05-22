from Monomio import Monomio
from Polinomio import Polinomio
from Edo import Edo

# f'(x) = 37.5 - 3.5y
polinomio = Polinomio()
polinomio.monomios.append(Monomio(37.5, '', 0))
polinomio.monomios.append(Monomio(-3.5, 'y', 1))

x = 0
y = 50
h = 1.5
edo = Edo(polinomio, h)

for i in range(0,3):
    print('{0}, {1}, {2}, {3}'.format(i, x, y, edo.euler(x, y)))
    x += h
    y = edo.euler(x, y)
