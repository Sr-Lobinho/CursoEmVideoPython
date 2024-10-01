r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1+r2>r3 and r1+r3>r2 and r3+r2>r1:
    print("As tres retas podem formar um triangulo", end = ". ")
    if r1 == r2 == r3:
        print("O triângulo é um triângulo equilátero")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("O triângulo é um triângulo isósceles")
    else:
        print("O triângulo é um triângulo escaleno")
else:
    print("As tres retas não podem formar um triangulo")
