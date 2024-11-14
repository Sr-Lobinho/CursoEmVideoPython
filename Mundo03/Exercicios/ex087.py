matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = st = ms = 0
for y in range(0,3):
    for x in range (0,3):
        matriz[y][x] = int(input(f"Digite um valor para [{y, x}]: "))

for y in range(0,3):
    for x in range(0,3):
        print(f"[{matriz[y][x]}]", end="")
    print()

for y in matriz:
    for p, x in enumerate(y):
        if x % 2 == 0:
            sp += x
        if p == 2:
            st += x


print(f"A soma dos valores pares é {sp}")
print(f"A soma dos valores da terceira coluna é {st}")
print(f"O maior valor da segunda linha é {max(matriz[1])}")