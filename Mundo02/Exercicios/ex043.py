peso = float(input("Dígite seu peso em quilos: "))
altura = float(input("Dígite sua altura em metros: "))

imc = peso / altura ** 2

print(f"Seu IMC é {imc:.1f}")

if imc < 18.5:
    print("Está abaixo do peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")