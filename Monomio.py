class Monomio:
    def __init__(self, coeficiente, literal, exponente):
        self.coeficiente = coeficiente
        self.literal = literal
        self.exponente = exponente

    def evaluar(self, n):
        return self.coeficiente * pow(n, self.exponente)
