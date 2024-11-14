lista = list()
dados = list()
maior = menor = 0


while True:
    
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])

    dados.clear()

    escolha = input("Você quer continuar? [S/N] ").lower().strip()
    while escolha not in "sn":
        escolha = input("Escolha inválida! Você quer continuar? [S/N] ").lower().strip()
    if escolha == "n":
        break


print(f"Os dados foram {lista}")
print(f"Ao todo, você cadastrou {len(lista)} pessoas.")
print(f"O maior peso foi de {maior:.1f}Kg. Peso de ", end="")
for p in lista:
    if p[1] == maior:
        print(p[0], end=" ")
print(f"\nO menor peso foi de {menor:.1f}Kg. Peso de ")
for p in lista:
    if p[1] == menor:
        print(p[0], end=" ")
