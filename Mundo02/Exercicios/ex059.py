from time import sleep

print("Dígite 2 valores")
v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo valor: "))
r = 0
opcao = 0

while opcao != 5:

    opcao = int(input("""Escolha uma opção:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    Opção: """))
    sleep(1)

    if opcao == 1:
        r = v1 + v2
        print(f"A soma de {v1} e {v2} é: {r}")
    elif opcao == 2:
        r = v1 * v2
        print(f"A multiplicação entre {v1} e {v2} resulta em: {r}")
    elif opcao == 3:
        maior = [v1, v2]
        print(f'O número {max(maior)} é maior do que {min(maior)}.')
    elif opcao == 4:
        v1 = int(input("Primeiro valor: "))
        v2 = int(input("Segundo valor: "))
    elif opcao != 5:
        print("Opção invalidade tente novamente!")
    sleep(1)
print("Programa desligado!")
