num = []
for i in range(0, 5):
    num.append(int(input(f"Digite um valor para a posição {i}: ")))

print(f"Você digitou os valores {num}")
print(f"O maior valor digitado foi {max(num)} nas posições ", end= "")
for m,n in enumerate(num):
    if n == max(num):
        print(m, end="... ")

print(f"\nO menor valor digitado foi {min(num)} nas posições ", end= "")
for a,b in enumerate(num):
    if b == min(num):
        print(a, end="... ")
