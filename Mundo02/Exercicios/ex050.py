print("Dígite seis números e veja somente a soma dos números pares que escolher.")
c = 0
s = 0
for p in range(1, 7):
    n = int(input(f"Número {p}: "))
    if n % 2 == 0:
        s += n
        c += 1
print(f"A soma dos {c} números pares escolhidos foi {s}")