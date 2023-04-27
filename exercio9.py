login=[]
senhas=[]

for i in range (0,5,1):
    login.append(input("Digite seu login:"))
    senhas.append(input("Digite sua senha:"))

for x in range(5):
    print(f"{x +1}-{login[x]}-{senhas[x]}")
