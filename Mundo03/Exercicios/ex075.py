n1 = int(input("Dígite um número: "))
n2 = int(input("Dígite outro número: "))
n3 = int(input("Dígite mais um número: "))
n4 = int(input("Dígite o último número: "))

tupla = (n1, n2, n3, n4)
print(f"Você digitou os valores {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes.")

if 3 in tupla:
    print(f"O valor 3 foi digitado na {tupla.index(3)}ª posição.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
print("Os valores pares digitados foram: ", end="")
for n in tupla:
    if n % 2 == 0:
        print(n, end= " ")