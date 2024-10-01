preco = float(input("Digite o preço do produto: "))
pagamento= int(input("""Qual será a forma de pagamento--
[1] À vista
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Opção: """))
total = preco
if pagamento == 1:
    total -= preco/10
    print(f"O total a ser pago será de R${total:.2f}")
elif pagamento == 2:
    total -= preco/20
    print(f"O total a ser pago será de R${total:.2f}")
elif pagamento == 3:
    print(f"O total a ser pago será de R${total:.2f} em 2 parcelas de R${total/2:.2f}")

elif pagamento == 4:
    parcelas = int(input("Em quantas parcelas? "))
    total += preco/5
    print(f"O total a ser pago será de R${total:.2f} em {parcelas} de R${total/parcelas:.2f}")
else:
    print("Opção invalida! Tente novamente")