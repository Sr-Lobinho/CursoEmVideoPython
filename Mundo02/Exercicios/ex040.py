n1 = float(input("Coloque sua primeira nota: "))
n2 = float(input("Coloque sua segunda nota: "))

media = (n1 + n2) / 2

if media < 5:
    print("Você está reprovado!")
elif media <= 6.9:
    print("Você está de recuperação!")
else:
    print("Você está aprovado!")