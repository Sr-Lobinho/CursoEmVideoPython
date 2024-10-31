expr = str(input("Dígite a expressão: "))
lista = []
for char in expr:
    if char == "(":
        lista.append(char)
    elif char == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(char)
            break

if len(lista) == 0:
    print("Sua expressão é valida!")
else:
    print("Sua expressão é invalida!")