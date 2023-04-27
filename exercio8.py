numeros=[]

for i in range (5):
    numeros.append(int(input("Digite um número:")))


for x in range (5):
    print(numeros[4-x], end=" ")
print()
print(numeros)
