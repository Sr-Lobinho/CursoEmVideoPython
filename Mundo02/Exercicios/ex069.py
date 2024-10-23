adulto = homem = mulher20 = 0
while True:
    print(25 * "-")
    print("  CADASTRE UMA PESSOA  ")
    print(25 * "-")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip()

    while sexo not in "mMfF":
        sexo = input("Sexo [M/F] ").strip()

    if idade >= 18:
        adulto += 1
    if sexo in "mM":
        homem += 1
    elif idade < 20:
        mulher20 += 1

    escolha = input("Você quer continuar? [S/N] ")
    while escolha not in "nNsS":
        escolha = input("Você quer continuar? [S/N] ")

    if escolha in "nN":
        break


print(f"""{6*"="} FIM DO PROGRAMA {6*"="}
Total de pessoa com mais de 18 anos: {adulto}
Ao todo temos {homem} homens cadastrados
E temos {mulher20} mulheres com menos de 20 anos""")
