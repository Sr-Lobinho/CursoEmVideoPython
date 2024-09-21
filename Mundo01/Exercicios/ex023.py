"""num = str(input("Digite um número: "))
uni = num[3]
dez = num[2]
cen = num[1]
mil = num[0]"""
num = int(input("Digite um número: "))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print(f"Unidade: {uni}\nDezena: {dez}\nCentena: {cen}\nMilhar: {mil}")