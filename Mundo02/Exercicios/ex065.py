escolha = "s"
s = quantidade = m = maior = menor = 0

while escolha in "Ss":
    n = int(input("Dígite um número: "))
    s += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    escolha = input("Quer continuar? [S/N]: ").strip()[0]

m = s / quantidade

print(f"Você digitou {quantidade} números \nO maior número foi {maior}, o menor número foi {menor} e a média foi {m}")