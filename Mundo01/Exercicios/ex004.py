algo = input("Digite algo: ")
print(type(algo))
print(f"Só tem espaços? {algo.isspace()}")
print(f"É um número? {algo.isnumeric()}")
print(f"É alfabético? {algo.isalpha()}")
print(f"É alfanumérico? {algo.isalnum()}")
print(f"Está em maiúscula? {algo.isupper()}")
print(f"Está em minúscula? {algo.islower()}")
print(f"Está capitalizado? {algo.istitle()}")
