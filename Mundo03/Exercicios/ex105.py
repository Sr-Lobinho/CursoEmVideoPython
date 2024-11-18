def notas(*n, sit=False):
    """
    — > Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais nótas dos alunos. (Aceita várias)
    :param sit: Valor opcional, indicando se deve ou não acionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dic ={
        'total' : len(n),
        'maior' : max(n),
        'menor' : min(n),
        'média' :  sum(n) / len(n)
    }
    if sit:
        if dic['média'] >= 7:
            dic['situação'] = "BOA"
        elif dic ['média'] >= 5:
            dic['situação'] = "RAZOÁVEL"
        else:
            dic['situação'] = "RUIM"
    return dic

resp = notas(7, 8, 9, sit=True )
print(resp)