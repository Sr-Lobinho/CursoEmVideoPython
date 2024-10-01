from random import choice
from time import sleep

print("Jokenpô!")
player = int(input("""Escolha uma das 3 opções:
[1] Pedra
[2] Papel
[3] Tesoura
Opção: """))

print("Pedra!")
sleep(1)

print("Papel!")
sleep(1)

print("Tesoura!!")
sleep(1)

lista = ["Pedra", "Papel", "Tesoura"]
pc = choice(lista)

print(f"Escolha do computador: {pc}")

if pc == "Pedra":
    if player == 1:
        print("Escolha do jogador: Pedra")
        print("Empate")
    elif player == 2:
        print("Escolha do jogador: Papel")
        print("O jogador ganhou!")
    elif player == 3:
        print("Escolha do jogador: Tesoura")
        print("O computador ganhou!")
    else:
        print("Opção invalida tente novamente")
elif pc == "Papel":
    if player == 1:
        print("Escolha do jogador: Pedra")
        print("O computador ganhou!")
    elif player == 2:
        print("Escolha do jogador: Papel")
        print("Empate")
    elif player == 3:
        print("Escolha do jogador: Tesoura")
        print("O jogador ganhou!")
    else:
        print("Opção invalida tente novamente")
elif pc == "Tesoura":
    if player == 1:
        print("Escolha do jogador: Pedra")
        print("O jogador ganhou")
    elif player == 2:
        print("Escolha do jogador: Papel")
        print("O computador ganhou!")
    elif player == 3:
        print("Escolha do jogador: Tesoura")
        print("Empate")
    else:
        print("Opção invalida tente novamente")

