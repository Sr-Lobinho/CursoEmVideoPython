jogador = {
    'nome' : str(input("Nome: ")),
    'partidas' : int(input("Total de partidas: ")),
    'total' : 0
}

for i in range(1, jogador['partidas'] + 1):
    jogador[f'partida {i}'] = int(input(f"Gols na partida {i}: "))
    jogador['total'] += jogador[f'partida {i}']

print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")

for k, v in jogador.items():
    if k == 'nome' or k =='partidas' or k == 'total':
        pass
    else:
        print(f"    => Na {k}, fez {v} gols.")
print(f"Foi um total de {jogador['total']} gols.")