soma = 0
sub20f =0
velhonome = ""
velhoidade = 0
for p in range(1, 5):

    print(f"{p}ª PESSOA:")
    nome = input("Dígite seu nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().lower()
    if sexo == "f" and idade < 20:
        sub20f += 1

    if p == 1 and sexo == "m":
        velhonome = nome
        velhoidade = idade
    if sexo == "m" and idade > velhoidade:
        velhonome = nome
        velhoidade = idade

    soma += idade

media = soma / 4

print(f"A média da idade do grupo é {media}\nA quantidade de mulheres com menos de 20 anos é {sub20f}\nE o homem mais velho é o {velhonome} com {velhoidade} anos")