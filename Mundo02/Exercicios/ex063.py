
n = int(input("Digite quantos termos você deseja: "))

t1 = 0
t2 = 1
c = 3

print(f"{t1} -> {t2}", end= "")

while c <= n:
    t3 = t1 + t2
    print(f" -> {t3}", end= "")
    t1 = t2
    t2 = t3
    c += 1

