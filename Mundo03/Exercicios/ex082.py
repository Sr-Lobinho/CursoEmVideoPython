num = []
impar = []
par = []
while True:
    n = int(input("Dígite um valor: "))
    num.append(n)
    if n % 2 ==0:
        par.append(n)
    else:
        impar.append(n)
    escolha = input("Você quer continuar? [S/N] ").lower().strip()
    while escolha not in "sn":
        escolha = input("Escolha inválida! Você quer continuar? [S/N] ").lower
    if escolha == "n":
        break
print(f"Números dígitados {num}")
print(f"Números pares digitados {par}")
print(f"Números ímpares digitados {impar}")