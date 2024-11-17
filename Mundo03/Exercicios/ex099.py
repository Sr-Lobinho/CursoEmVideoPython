from time import sleep

def maior(*num):
    m = 0
    print(30*"-=")
    for i, n in enumerate(num):
        print(n, end= " ")
        if i == 0:
            m = n
        elif n > m:
            m = n
        sleep(0.4)
    print(f"Foram informados {len(num)} valores ao todo")
    print(f"O maior valor informado foi {m}")

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()