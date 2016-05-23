from Monomio import Monomio
from Polinomio import Polinomio
from Integracion import Integracion
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

print("i  x\t y\t yi+1")
while x1 <= x2:
    print('{0}  {1}\t {2}\t {3}'.format(i, x1, y, edo.rungeKutta4(x1, y)))
    y = edo.rungeKutta4(x1, y)
    x1 += h
    i += 1


# Integracion
# f'(x) = 0.0003x^2 - 0.12x + 20
polinomio = Polinomio()
polinomio.monomios.append(Monomio(0.0003, 'x', 2))
polinomio.monomios.append(Monomio(-0.12, 'x', 1))
polinomio.monomios.append(Monomio(20, '', 1))

integracion = Integracion(polinomio)
print(integracion.simpsonUnTercio(0, 300))
