lista = []
for i in range(1, 6):
    peso = float(input(f"Dígite o peso da pessoa {i}: "))
    lista.append(peso)
lista.sort()
print(f"O menor peso foi {lista[0]}Kg e o maior peso foi {lista[4]}Kg")