def escreva(msg):
    tamanho = len(msg) + 4
    print("~" * tamanho)
    print(f"{msg:^{tamanho}}")
    print("~" * tamanho)

escreva("CeV")
escreva("CURSO EM VÍDEO")