def somar(a,b):
    soma = a+b
    return soma
def subtrair(a,b):
    sub = a-b
    return sub
def multiplicar(a,b):
    mult = a*b
    return mult
def divisao(a,b):
    div = a/b
    return div

op=10
while op!=0:

    n1 = int(input("Digite o primeiro numero:"))
    n2 = int(input("Digite o segundo numero:"))

    print("escolha a operação a seguir")
    print("(1) para somar")
    print("(2) para subtrair")
    print("(3) para multiplicar")
    print("(4) para dividir")
    print("(0) para sair")

    op= int(input("Escolha a operação:"))

    match op:
        case 1:
            print(somar(n1,n2))
        case 2:
            print(subtrair(n1,n2))
        case 3:
            print(multiplicar(n1,n2))
        case 4:
            print(divisao(n1,n2))











