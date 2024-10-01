num = int(input("Dígite um número para converter: "))
escolha = int(input("""Escolha uma das opções abaixo para converter:
 [1] Binário
 [2] Hexadecimal
 [3] Octal
 Opção: """))
if escolha == 1:
    print(f"Binário: {bin(num)[2:]}")
elif escolha == 2:
    print(f"Hexadecimal: {hex(num)[2:]}")
elif escolha == 3:
    print(f"Octal: {oct(num)[2:]}")
else:
    print("Nenhuma opção selecionada!")
