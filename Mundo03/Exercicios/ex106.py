def escreva(msg, cor):
    tamanho = len(msg) + 4
    print(cor, end="")
    print("~" * tamanho)
    print(f"{msg:^{tamanho}}")
    print("~" * tamanho, )


while True:
    escreva("SISTEMA DE AJUDA PyHelp", "\033[44;97m")
    opcao = input("\033[mFunção ou Biblioteca > ")
    if opcao.strip().lower() == "fim":
        break
    escreva(f"Acessando o manual do comando '{opcao}'", "\033[45;97m")
    print("\033[7;40;97m")
    help(opcao)
    print("\033[m", end="")

escreva("ATÉ LOGO!", "\033[41;97m")