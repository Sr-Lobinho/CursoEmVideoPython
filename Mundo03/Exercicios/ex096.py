def area(l, c):
    a = l * c
    print(f"A área de um terreno {l}x{c} é de {a}m².")

print("Controle de Terrenos")
print(25*"-")
area(float(input("LARGURA (m): ")), float(input("COMPRIMENTO (m): ")))