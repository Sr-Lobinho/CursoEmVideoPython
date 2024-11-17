from time import sleep

def contador(a1, an, r):
    if r < 0:
        r *= -1
    elif r == 0:
        r = 1
    print(20 * "-=")
    print(f"Contagem de {a1} até {an} de {r} em {r}")
    if a1 > an:
        r *= -1
        an -= 2
    for a in range(a1, an+1, r):
        print(a,  end=" ")
        sleep(0.2)
    print("FIM!")

contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é a sua vez de personalizar a contagem!")
contador(int(input("Ínicio: ")), int(input("Fim: ")), int(input("Passo: ")))