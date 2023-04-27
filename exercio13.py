nomes=[]
for i in range(5):
    nomes.append(input("Digite o nome do aluno:"))
print(nomes)

for y in range(4,-1,-1):
    print(f"{y+1}-{nomes[y]}")

