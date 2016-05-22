error = 0.0005

coef = [2, 3, -10]
expo = [2, 1, 0]
cal = 0;

def evaluarFuncion(x) :
    res = 0
    for i, item in enumerate(coef) :
        res += pow(x, expo[i]) * coef[i]
    return res

def signo(a, b) :
    return a * b > 0

def encuentraRaiz(a, b):
    i = 0
    fc = 1

    while i < 100 and abs(fc) > error:
        c = (a+b)/2
        fa = evaluarFuncion(a)
        fb = evaluarFuncion(b)
        fc = evaluarFuncion(c)

        print('{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(i, a, b, c, fa, fb, fc))

        if( signo(fa, fc) ):
            a = c
        if( signo(fb, fc) ):
            b = c

        i+=1

encuentraRaiz(1, 2)
