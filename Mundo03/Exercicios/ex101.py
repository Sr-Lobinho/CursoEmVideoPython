def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return "NÃO VOTA" , idade
    elif idade < 18 or idade > 65:
        return "VOTO OPCIONAL" , idade
    else:
        return "VOTO OBRIGATÓRIO" , idade

nasc = int(input("Em que ano você nasceu? "))
print(f"Com {voto(nasc)[1]} anos: {voto(nasc)[0]}")