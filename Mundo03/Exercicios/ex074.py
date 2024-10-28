from random import randint
sorteado = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print("Os números sorteados foram: ", end="")

for n in sorteado:
    print(n, end=" ")

print(f"\nO maior valor sorteado foi {max(sorteado)} e o menor valor sorteado foi {min(sorteado)}")

