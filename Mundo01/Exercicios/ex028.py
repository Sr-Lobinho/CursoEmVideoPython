from random import randint
print("Tente descobrir o número em que eu estou pensando.")
num = randint(0,5)
chute = int(input("Digite um número de 0 a 5: "))
if chute == num:
    print("Parabéns você acertou!")
else:
    print("Mais sorte na próxima")