from random import randint
from time import sleep
dados = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
print("Valores sorteados: ")
for p, d in dados.items():
    print(f"O {p} tirou {d}")
    sleep(1)
print("Ranking dos jogadores: ")
c = 1
for p, d in sorted(dados.items(), key=lambda item: item[1], reverse= True):
    print(f"{c}º lugar: {p} com {d}")
    c += 1
    sleep(1)