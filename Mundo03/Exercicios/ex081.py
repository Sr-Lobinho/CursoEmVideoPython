num = []
while True:
    n = int(input("Dígite um valor: "))
    num.append(n)
    escolha = input("Você quer continuar? [S/N] ").lower().strip()
    while escolha not in "sn":
        escolha = input("Escolha inválida! Você quer continuar? [S/N] ").lower
    if escolha == "n":
        break



print(f"Foram digitados {len(num)} números.")
print(f"Os valores em ordem decrescente são {sorted(num, reverse= True)}")
print("O número 5 foi dígitado e está na lista"if 5 in num else "O número 5 não foi digitado")