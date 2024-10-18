n = int(input("Dígite um número [Digite 999 para parar]: "))
"""s = 0
c = 0"""
s = c = 0
while n != 999:
    s += n
    c += 1
    n = int(input("Digite um número [Digite 999 para parar] : "))

print(f"Você digitou {c} números somando {s}")