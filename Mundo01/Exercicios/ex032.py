from datetime import date
ano = int(input("Digite um ano: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano \033[34m{ano}\033[m \033[32mé\033[m bissexto!")
else:
    print(f"O ano \033[34m{ano}\033[m \033[31mnão é\033[m bissexto")