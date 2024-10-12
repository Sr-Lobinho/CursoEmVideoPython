r = int(input("Dígite um número para descobrir quantos números primos existe entre 1 e o número: "))
c = 0
contadorp = 0
for ii in range(1, r + 1):
    n = ii
    for i in range(1,n + 1):
        if n % i == 0:
            print("\033[32m", end= " ")
            c += 1
        else:
            print("\033[31m", end= " ")
        print(f"{i}", end= " ")
    if c == 2:
        print("\n\033[mÉ um número primo!")
        contadorp +=1

    else:
        print("\n\033[mNão é um número primo!")
    c = 0
print(f"Entre 1 e {r} existem {contadorp} números primos")