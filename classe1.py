class Pessoas:
    # so usa o init uma unica vez na classe
    def __init__(self, nome, peso, idade, comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
# funçao comendo
    def comer(self,comida):
      if self.comendo:
        # parametro
        self.comida=comida
        # flag=sinaliza
        self.comendo=True
        print(f'{self.nome} está comendo {self.comida}')
      else:
        print(f'{self.nome} não pode comer,pois já esta comendo')

    def pararcomer(self):
       if self.comendo == True:
           self.comendo=False
          # dentro do if pra nao da erro: ...
       else:
           print("Não está comendo")

    def falar(self):
        if self.comendo:
            self.comida = comida
            self.comendo = True
            print(f'{self.nome} está falando {self.comida}')
        else:
            print(f'{self.nome} não pode falar,pois esta comendo')






p1= Pessoas("Joao",80,19,)
p2= Pessoas("Maria",54,28,)
p3= Pessoas("Pedro",53,19,True)

p1.falar()
p2.comer("laranja")
# p1.comer("banana")
p3.comer("uva")

# print(f'{p1.nome} pesa {p1.peso}kg e tem {p1.idade} anos')
# print(vars(p2))
# # biblioteca
# print(vars(p3))
# # estudar bastante essa parte
