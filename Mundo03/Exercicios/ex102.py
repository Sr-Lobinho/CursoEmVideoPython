def fatorial(num, show=False):
    """
    → Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor Fatorial de num.
    """
    f = 1
    c = num
    r = ""
    while c > 1:
        f *= c
        r += f"{c} x "
        c -= 1
    r += f"1 = {f}"
    if show:
        return r
    else:
        return f

print(fatorial(5, True))
help(fatorial)