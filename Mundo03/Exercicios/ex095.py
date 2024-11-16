jogadores = list()
while True:
    jogador = {
        'nome' : str(input("Nome: ")),
        'partidas' : int(input("Total de partidas: ")),
        'gols' : list()
    }

    for i in range(0, jogador['partidas']):
        jogador['gols'].append(int(input(f"Quantos gols na partida {i}? ")))

    jogadores.append(jogador.copy())
    jogador.clear()

    escolha = input("Você quer continuar? [S/N] ").lower().strip()
    while escolha not in "sn":
        escolha = input("Escolha inválida! Você quer continuar? [S/N] ").lower().strip()
    if escolha == "n":
        break
print(30 * "-=")

print(f"cod {"nome":<10} {"gols":<20} total")
print(40 * "-")
for n, p in enumerate(jogadores):
    print(f"{n:<3} {p['nome']:<10} {f"{p['gols']}":20} {sum(p['gols']):<5}")
while True:
    print(40 * "-")
    escolha = int(input("Mostrar dados de qual jogador? (999 interrompe): "))
    if escolha == 999:
        break
    elif escolha >= len(jogadores):
        print(f"ERRO! Não existe jogador com código {escolha}! Tente novamente")
    else:
        for n ,g in enumerate(jogadores[escolha]['gols']):
            print(f"No jogo {n} fez {g} gols.")
print("<<<VOLTE SEMPRE>>>")