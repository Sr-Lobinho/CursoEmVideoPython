from random import randint
from time import sleep
jogos = int(input("Quantos jogos você quer que eu sorteie? "))

for jogo in range(0,jogos):
    numeros = []
    for n in range(0, 6):
        num = randint(1,60)
        while num in numeros:
            num = randint(1, 60)
        numeros.append(num)
    sleep(1)
    print(f"Jogo {jogo + 1}: {numeros}")
