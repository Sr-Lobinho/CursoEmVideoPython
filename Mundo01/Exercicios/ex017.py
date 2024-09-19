from math import hypot
cop = float(input("Digite o comprimento do cateto oposto: "))
cad = float(input("Digite o comprimento do cateto adjacente: "))
#hip = (cop**2 + cad **2)**(1/2)
hip = hypot(cop,cad)
print(f"A hipotenusa desse triangulo retângulo é {hip:.2f}")