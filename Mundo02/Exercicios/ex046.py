from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print("\033[31mBOOM!!\033[m")