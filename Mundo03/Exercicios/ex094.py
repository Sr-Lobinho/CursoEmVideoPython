lista = list()
media = 0
while True:
    pessoa = {
        'nome' : str(input("Nome: ")),
        'sexo' : str(input("Sexo: [M/F] ")).strip().upper(),
        'idade' : int(input("Idade: "))
    }
    lista.append(pessoa.copy())

    media += pessoa['idade']

    pessoa.clear()

    escolha = input("Você quer continuar? [S/N] ").lower().strip()
    while escolha not in "sn":
        escolha = input("Escolha inválida! Você quer continuar? [S/N] ").lower().strip()
    if escolha == "n":
        break

media = media / len(lista)

print(f"O grupo tem {len(lista)} pessoas.")
print(f"A média de idade é de {media:5.2f} anos")
print("As mulheres cadastradas foram: ", end= "")

for p in lista:
    if p['sexo'] == "F":
        print(p['nome'], end= " ")

print("\nLista das pessoas que estão acima da média: ")

for p in lista:
    if p['idade'] >= media:
        print(f"nome = {p['nome']}: sexo = {p['sexo']}: idade = {p['idade']}")



