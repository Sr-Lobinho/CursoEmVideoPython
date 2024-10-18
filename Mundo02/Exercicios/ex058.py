from random import randint
print("Tente descobrir o número em que eu estou pensando.")
num = randint(0,10)
chute = int(input("Digite um número de 0 a 10: "))
tentativas = 1
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while chute != num:
    if chute not in lista:
        chute = int(input("Digite um número valido de 0 a 10: "))
    else:
        chute = int(input("Tente denovo: "))
    tentativas +=1
print(f"Parabéns você acertou em {tentativas} tentativas!")
