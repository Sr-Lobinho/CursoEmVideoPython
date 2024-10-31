numeros = []
for i in range(0, 5):
    num = int(input("Digite um valor: "))
    if i == 0 or num > numeros[-1]:
        numeros.append(num)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f"Adicionado na posição {pos} da lista")
                break
            pos += 1

print(numeros)