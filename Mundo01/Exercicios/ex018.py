from math import sin, cos, tan, radians
angulo = float(input("Digite um angulo: "))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f"Esse angulo possui:\nSeno = {sen:.2f}\nCosseno = {cos:.2f}\nTangente = {tan:.2f}")