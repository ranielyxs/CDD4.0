notas=[]
for i in range (5):
    notas.append(float(input("digite a nota:")))

soma=0
for x in range(5):
    soma += notas[x]
media=soma/5
print("A media da turma é:",media)
cont=0
for j in range(5):
    if media<=notas [j]:
        cont+=1