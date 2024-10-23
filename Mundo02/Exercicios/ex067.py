while True:
    n = int(input("Você quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("-"*30)
    for c in range(1, 11):
        print(f"{n} X {c:2} = {n * c}")
    print("-" * 30)
print("PROGRAMA ENCERRADO!")

