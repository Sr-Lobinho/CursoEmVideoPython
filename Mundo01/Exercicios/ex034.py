salario = float(input("Dígite seu sálario: "))
if salario >= 1250.00:
    aumento = salario / 10
else:
    aumento = salario * 15 /100
print(f"Você receberá um aumento de \033[34mR${aumento}\033[m e seu novo salário será de \033[35mR${salario + aumento}\033[m")