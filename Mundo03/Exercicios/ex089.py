alunos = list()

while True:
    aluno = [str(input("Nome: ")), [float(input("Nota 1: ")), float(input("Nota 2: "))]]
    media = (aluno[1][0] + aluno[1][1])/2
    aluno[1].append(media)
    alunos.append(aluno[:])

    aluno.clear()

    escolha = input("Você quer continuar? [S/N] ").lower().strip()
    while escolha not in "sn":
        escolha = input("Escolha inválida! Você quer continuar? [S/N] ").lower().strip()
    if escolha == "n":
        break

print(30*"-=")
print(f"{"No.":<5} {"NOME":<10} MÉDIA")
print(25*"-")
for num, aluno in enumerate(alunos):
    print(f"{num:<5} {aluno[0]:<10} {aluno[1][2]}")

print(25*"-")
while True:
    escolha = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if escolha == 999:
        break
    if escolha <= len(alunos) - 1:
        print(f"Notas de {alunos[escolha][0]} são {alunos[escolha][1][0:2]}")
