alunos = {}
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
print('-=' * 30)
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['media'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
for k, v in alunos.items():
    print(f'- {k} é igual a {v}')






