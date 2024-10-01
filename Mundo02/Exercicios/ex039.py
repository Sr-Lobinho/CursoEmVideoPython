from datetime import date
nascimento = int(input("Coloque o ano em que você nasceu: "))
idade = date.today().year - nascimento

if idade < 18:
    print(f"Ainda faltam {18-idade} ano(s) para você se alistar")
elif idade == 18:
    print("Você deve fazer o alistamento este ano")
elif idade > 18:
    print(f"Você deveria ter se alistado há {idade - 18} anos")