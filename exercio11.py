a= []
b=[]
c=[]
tam=int(input("Digite o tamanho do array:"))
for i in range(tam):
    a.append(int(input("Digite um valor para A:")))
    b.append(int(input("Digite um valor para B:")))

for y in range(tam):
    c.append(a[y] + b[y])
print(a)
print(b)
print(c)
