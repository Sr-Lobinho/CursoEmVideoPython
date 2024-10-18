n = int(input("Digite um número para fatoriar: "))
c = n
f = 1

while n !=0:
    f *= n
    n -= 1

print(f"O fatorial de {c} é {f}")