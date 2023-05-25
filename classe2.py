class Banco:
    def __init__(self,nome,numero_da_conta,tipo_de_conta,limite,saldo=0,status=False):
        self.nome=nome
        self.numero_da_conta=numero_da_conta
        self.tipo_de_conta=tipo_de_conta
        self.status= status
        self.saldo = saldo
        self.limite=limite

    def ativar(self):
        if self.status ==False:
         self.status=True
         print(f'{self.nome} sua conta foi ativada')

    def depositar(self, valor):
     self.saldo += valor
     print("Depósito realizado. Novo saldo:", self.saldo)


    def sacar(self, valor):
     if self.saldo >= valor:
        print("Saque realizado. Novo saldo:", self.saldo)


    def obter_saldo(self):
     print("Saldo atual:", self.saldo)

    def desativar(self):
        if self.saldo < 0:
            self.ativa = False
            print("conta desativada saldo negativo.")

    def limite_especial(self,limite):
        if self.limite:
            self.saldo=False
            print("Limite liberado",limite)



c1= Banco("Maria",12003,"Conta-corrente",True)
print(vars(c1))
c1.ativar()
c1.depositar(10)
c1.sacar(300)
c1.obter_saldo()
c1.desativar()
c1.limite_especial(1000)



