palavras = ("abacate", "pera", "uva", "banana", "mexerica")
vogais = ("a", "e", "i", "o", "u")
for palavra in palavras:
    print(f"Na palavra {palavra} temos ", end="")
    for letra in palavra:
        if letra in vogais:
            print(letra, end= " ")
    print("")