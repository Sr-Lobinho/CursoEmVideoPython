from random import shuffle
a1 = input("Escolha o primeiro aluno: ")
a2 = input("Escolha o segundo aluno: ")
a3 = input("Escolha o terceiro aluno: ")
a4 = input("Escolha o quarto aluno: ")
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f"A ordem sorteada foi: {alunos}")
