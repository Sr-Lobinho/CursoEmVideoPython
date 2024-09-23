r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1+r2>r3 and r1+r3>r2 and r3+r2>r1:
    print("As tres retas \033[35mpodem\033[m formar um triangulo")
else:
    print("As tres retas \033[33mnão podem\033[m formar um triangulo")