def notas(*n,sit=False):
    """
       -> Função para analisar situação de vários alunos
       :param n: uma ou mais notas de alunos (aceita varias)
       :param sit: valor opcional, indicando se deve ou não indicar a situação
       :return: dicionário com várias informações da turma
       """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if r['media'] >= 7:
        r['situação'] = 'BOA'
    elif r['media'] >= 5:
        r['situação'] = 'RAZOÁVEL'
    else:
        r['situação'] = 'RUIM'
    return r


#Programa principal
resp = notas(5.6, 4.7, 8, 9)
print(resp)