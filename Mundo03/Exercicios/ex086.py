matriz = [[0,0,0],[0,0,0],[0,0,0]]
for y in range(0,3):
    for x in range (0,3):
        matriz[y][x] = int(input(f"Digite um valor para [{y, x}]: "))

for y in range(0,3):
    for x in range(0,3):
        print(f"[{matriz[y][x]:^5}]", end="")
    print()