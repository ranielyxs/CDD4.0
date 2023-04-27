a= []
m=[]
for i in range(10):
    a.append(int(input("Digite um número:")))
x=int(input("Digite o multiplicador:"))

for y in range(10):
    m.append(x*a[y])
print(a)
print(x)
print(m)


