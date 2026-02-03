def notas(*n,sit=False):
    """
        -> Função para analisar situação de vários alunos
        :param n: uma ou mais notas de alunos (aceita varias)
         :param sit: valor opcional, indicando se deve ou não indicar a situação
         :return: dicionário com várias informações da turma
           """
    alunos = dict()
    alunos['total'] = len(n)
    alunos['maior'] = max(n)
    alunos['menor'] = min(n)
    alunos['media'] = sum(n) / len(n)
    if sit:
        if alunos['media'] >= 7:
            alunos['situação'] = 'BOA'
        elif 7 > alunos['media'] < 5:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'RUIM'
    return alunos


#programa principal
resp = notas(9.5, 8.4, 2.9, 7.6, 10, sit=True)
print(resp)