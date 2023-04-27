login=[]
senhas=[]

for i in range (2):
    login.append(input("Digite seu login:"))
    senhas.append(input("Digite sua senha:"))

usuario=input("Informe seu login:")
senha= input("Informe sua senha:")

for x in range(2):
    if usuario == login[x] and senha == senhas[x]:
        print("Login efetuado com sucesso!")