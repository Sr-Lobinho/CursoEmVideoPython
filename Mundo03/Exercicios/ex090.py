relatorio = dict()
relatorio['Nome'] = str(input("Nome: "))
relatorio['Média'] = float(input(f"Média de {relatorio['Nome']}: "))
if relatorio['Média'] >= 6.0:
    relatorio['Situação'] = "Aprovado"
elif relatorio['Média'] >= 4.0:
    relatorio['Situação'] = "Recuperação"
else:
    relatorio['Situação'] = "Reprovado"

for k, v in relatorio.items():
    print(f"{k} é igual a {v}")