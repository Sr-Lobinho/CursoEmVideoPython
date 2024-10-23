total = mais1000 = baratop = 0
barato = ""
print(20*"-")
print(f"{4*" "}LOJA DE TUDO{4 * " "}")
print(20*"-")
while True:
    nome = input("Nome do Produto: ")
    preco = float(input("Digite o preço: R$"))
    if barato == "" or preco < baratop:
        barato = nome
        baratop = preco
    if preco > 1000:
        mais1000 += 1
    total += preco

    escolha = input("Você quer continuar? [S/N] ")
    while escolha not in "nNsS":
        escolha = input("Você quer continuar? [S/N] ")

    if escolha in "nN":
        break

print(f"""{11*"-"} FIM DO PROGRAMA {11*"-"}
O total da compra foi R${total:.2f}
Temos {mais1000:.2f} produtos custando mais de R$1000.00
O produto mais barato foi {barato} que custa R${baratop}""")