s = 0
c = 0
for n in range(3, 501, 3):
    if n % 2 != 0:
        c += 1
        s  += n

print(f"A soma de todos os {c} valores é igual a {s}")