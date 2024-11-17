from random import randint
from time import sleep

def sorteia(lst):
    print("Sorteado 5 valores da lista: ", end="")
    for i in range(0, 5):
        num = randint(0,10)
        print(num, end=" ")
        lst.append(num)
        sleep(0.5)
    print("PRONTO!")

def somaPar(lst):
    s = 0
    for num in lst:
        if num % 2 == 0:
            s += num
    print(f"Somando todos os valores pares de {lst}, temos {s}")

numeros = list()
sorteia(numeros)
somaPar(numeros)