q_alunos=int(input("Quantos alunos tem na sua sala de aula:"))
alunos= []
for i in range(q_alunos):
    alunos.append(input("Digite o nome do aluno:"))

for y in range(q_alunos):
    print(alunos[y],y)

nome = input("Qual a aluno deveria estar na lista?")
for x in range(q_alunos):
    if nome ==alunos [x]:
        print(alunos[k],k)
