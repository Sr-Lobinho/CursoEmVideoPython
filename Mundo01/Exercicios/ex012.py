preco = float(input("O preço do produto: R$"))
desconto = preco/20
novo_preco = preco - desconto
print(f"O desconto foi de R${desconto:.2f}\nO novo preço é R${novo_preco:.2f}")