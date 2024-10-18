sexo = input("Digite seu sexo [M/F]: ").strip()[0]
while sexo not in "MmFf":
    sexo = input("Digite uma das 2 opções [M/F]: ").strip()[0]
print(f"Sexo escolhido: {sexo}")