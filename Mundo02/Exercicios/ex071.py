valor = int(input("Que valor você quer sacar? R$"))

c50 = c20 = c10 = c1 = 0

while valor >= 50:
    valor -= 50
    c50 += 1
while valor >= 20:
    valor -= 20
    c20 += 1
while valor >= 10:
    valor -= 10
    c10 += 1
while valor >= 1:
    valor -= 1
    c1 += 1


print(f"""Total de {c50} cédulas de R$50
Total de {c20} cédulas de R$20
Total de {c10} cédulas de R$10
Total de {c1} cédulas de R$1""")