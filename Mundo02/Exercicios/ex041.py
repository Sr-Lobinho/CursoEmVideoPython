from datetime import date

nascimento = int(input("Dígite o ano em que você nasceu: "))
idade = date.today().year - nascimento

if idade <= 9:
    print("Mirím")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Júnior")
elif idade <= 25:
    print("Sênior")
else:
    print("Master")