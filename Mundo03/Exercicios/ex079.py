num = []
while True:
    n = int(input("Dígite um valor: "))
    if n not in num:
        num.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    escolha = input("Você quer continuar? [S/N] ").lower().strip()
    if escolha not in "sn":
        escolha = input("Escolha inválida! Você quer continuar? [S/N] ").lower
    elif escolha == "n":
        break


print(sorted(num))