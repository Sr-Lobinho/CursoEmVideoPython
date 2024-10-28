lista= ("Pão", 1, "Pizza", 12, "Café", 3.50, "Macarrão", 7.99, "Leite", 3.50)

print(f"{"Lista de Compras":^30}")
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<30}", end= "")
    else:
        print(f"R${lista[i]:>7.2f}")

