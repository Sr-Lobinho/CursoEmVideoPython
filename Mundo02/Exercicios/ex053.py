frase = input("Dígite uma frase para descobrir se ela é um palíndromo ou não: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for l in range(len(junto) -1, -1, -1):
    inverso += junto[l]
#inverso = junto[::-1]
print(f"Frase dígitada {junto}\nFrase ao contrario {inverso}")

if inverso == junto:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")