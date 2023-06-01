class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0
class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self, base, altura):
        self.base = base
        self.altura = altura
        return f'A área do retângulo é: {self.base * self.altura}'

    def calcuraPerimetro(self, base, altura):
        self.base = base
        self.altura = altura
        return f'O perimetro do retângulo é: {self.base*2 + self.altura*2}'


class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self, base, altura):
        self.base = base
        self.altura = altura
        return f'A área do triângulo é de: {self.base * self.altura/2}'

    def calcularPerimetro(self, base):
        self.base = base
        return f'O perimetro do triângulo é: {self.base*3}'

Retangulo = Retangulo()
print(Retangulo.calcularArea(15, 25))
print(Retangulo.calcuraPerimetro(15, 25))
Triangulo = Triangulo()
print(Triangulo.calcularArea(14, 14))
print(Triangulo.calcularPerimetro(25))