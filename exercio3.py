q_alunos=int(input("Quantos alunos tem na sua sala de aula?"))
alunos= []
for i in range(q_alunos):
    alunos.append(input("Digite o nome do aluno"))

for y in range(q_alunos):
    print(alunos[y],y)