from datetime import date
Dic = {
    'nome' : str(input("Nome: ")),
    'idade' : date.today().year - int(input("Ano de Nascimento: ")),
    'ctps' : input("Carteira de Trabalho (0 não tem): ")
}
if Dic['ctps'] != "0":
    Dic['contratação'] = int(input("Ano de contratação: "))
    Dic['salário'] = float(input("Sálario: R$"))
    Dic['aposentadoria'] = ( Dic['contratação'] + 35) - (date.today().year - Dic['idade'])

for k, v in Dic.items():
    print(f"{k} tem o valor {v}")