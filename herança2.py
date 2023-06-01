class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        return f'O valor do ingresso é: R${self.valor} reais'



class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional


    def PreçoCompl(self):
        return f'O valor do ingresso VIP é: R${self.valor+self.adicional} reais'



Ingresso1 = Ingresso(568)
print(Ingresso1.imprimir())
Ingresso2 = VIP(568, 315)
print(Ingresso2.PreçoCompl())



