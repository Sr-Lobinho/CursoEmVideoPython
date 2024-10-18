print("--- Criando uma PA de 10 termos ---")

a1 = int(input("Dígite o primeiro termo: "))
r = int(input("Dígite a razão da PA: "))
a10 = a1 +(10 -1) *r
an = a1
while an != a10:
    print(an, end= " -> ")
    an += r
print(a10)