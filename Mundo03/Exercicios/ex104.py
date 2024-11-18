def leiaInt(txt):
    while True:
        i = str(input(txt))
        if i.isnumeric():
            i = int(i)
            break
        print("\033[31m ERRO! Dígite um número válido.\033[m")
    return i


n = leiaInt("Dígite um número: ")
print(f"Você acabou de dígitar o número {n}")
