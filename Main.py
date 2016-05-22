from Monomio import Monomio
from Polinomio import Polinomio
from Edo import Edo

# f'(x) = -y + x2
polinomio = Polinomio()
polinomio.monomios.append(Monomio(-1, 'y', 1))
polinomio.monomios.append(Monomio(1, 'x', 2))

x = 0
y = 1
h = 0.5
edo = Edo(polinomio, h)

for i in range(0,7):
    print('{0}, {1}, {2}, {3}'.format(i, x, y, edo.euler(x, y)))
    y = edo.euler(x, y)
    x += h
