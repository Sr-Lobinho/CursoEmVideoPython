print("--- Criando uma PA de 10 termos ---")
a1 = int(input("Dígite o primeiro termo: "))
r = int(input("Dígite a razão da PA: "))
a10 = a1 +(10 -1) *r

for an in range(a1, a10, r):
    print(an, end= " -> ")
print(f"{a10}")