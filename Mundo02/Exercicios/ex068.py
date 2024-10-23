from random import randint
print("=-" * 10)
print("PAR OU ÍMPAR")
print("=-" * 10)
v = 0
while True:
    cpu = randint(1,10)
    player = int(input("Diga um valor: "))
    escolha = input("Par ou Ímpar? [P/I] ")
    s = cpu + player
    resultado = "ÍMPAR"
    if s % 2 == 0:
        resultado = "PAR"
    print("-" * 20)
    print(f"Você jogou {player} e o computador {cpu}. Total de {s} DEU {resultado}")
    print("-" * 20)
    if resultado == "ÍMPAR" and escolha in "pP" or resultado == "PAR" and escolha in "iI":
        print("VOCÊ PERDEU!")
        print("=-" * 10)
        break
    print("VOCÊ VENCEU!")
    print("Vamos jogar novamente...")
    print("=-" * 10)
    v += 1
print(f"GAME OVER! Você venceu {v} vezes.")