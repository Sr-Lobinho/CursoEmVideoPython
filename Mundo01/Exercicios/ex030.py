num = int(input("Digite um número: "))
resultado = num % 2  #num / 2
if  resultado == 0: #resultado.is_integer():
    print("É \033[34mpar")
else:
    print("É \033[35mímpar")