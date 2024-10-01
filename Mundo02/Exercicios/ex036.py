print("Antes de fazer o empréstimo preencha as informações abaixo")

vcasa = float(input("O valor da casa: "))
salario = float(input("O seu salário: "))
anos = int(input("Em quantos anos você irá pagar: "))

prestacao = vcasa / (anos * 12)
print(f"Para pagar uma casa com valor de R${vcasa:.2f} em {anos} anos você precisará pagar uma prestação mensal de R${prestacao:.2f}")
if prestacao > salario * 30 /100:
    print("O empréstimo não poderá ser feito pois o valor da prestação mensal é maior que 30% do seu sálario")
else:
    print("O empréstimo será possível. Tenha um bom dia!")