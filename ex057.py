#Jeito mais fácil
sexo = str(input('Qual seu sexo[M/F]? ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados inválidos, por favor, infome seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')







#Jeito que eu fiz
'''masc = 'M'
fem = 'F'
sexo = ''
while sexo in 'M' and sexo in 'F':
    sexo = str(input('SEXO[M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Você digitou errado!')
        novo = str(input('Digite novamente. Sexo[M/F]: '))
print('FIM')
'''


