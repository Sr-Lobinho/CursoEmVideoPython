carteira = float(input("Quanto dinheiro você tem? R$"))
dolar = 5.63 #no video era 3,27
euro = 6.25
print(f"Com R${carteira:.2f} você pode comprar {carteira/dolar:.2f} dólares e {carteira/euro:.2f} euros")