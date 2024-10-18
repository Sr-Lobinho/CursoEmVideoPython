print("Gerador de PA")

a1 = int(input("Dígite o primeiro termo: "))
r = int(input("Dígite a razão da PA: "))
an = a1
c = 1
total = 0
termos = 10
print(a1, end= "")
while termos != 0:
    total += termos
    while c <= total:
        an += r
        c += 1
        print(" -> ", end= f"{an}")
    termos = int(input("\nQuantos termos a mais você quer? "))

print(f"PA finalizada com {total} termos")

