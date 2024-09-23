kmh = float(input("Digite a velocidade do carro: "))
if kmh > 80:
    print(f"Você ultrapassou o limite de velocidade e terá que pagar \033[1;31mR${7*(kmh-80):.2f}\033[m de multa")

else:
    print("Tenha um bom dia!")