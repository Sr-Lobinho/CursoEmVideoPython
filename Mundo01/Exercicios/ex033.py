n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Mais um número: "))
lista = [n1, n2, n3]
maior = max(lista)
menor = min(lista)
print(f"O maior número é \033[36m{maior}\033[m e o menor número é \033[35m{menor}\033[m")
