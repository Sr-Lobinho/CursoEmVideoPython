from datetime import date
c = 0
for i in range(1,8):
    ano = int(input(f"Dígite o ano de nascimento da pessoa {i}: "))
    if date.today().year - ano >= 21:
        c += 1

print(f"A quantidade de pessoas que não atingiram a maioridade é {7 - c}\nE a quantidade de maiores de idade é {c}")