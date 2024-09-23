distancia = int(input("Qual a distância da viagem em \033[35mkm\033[m? "))

if distancia <= 200:
    preço = 0.5 * distancia
else:
    preço = 0.45 * distancia
print(f"O preço da viagem será \033[33mR${preço:.2f}\033[m")