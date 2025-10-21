masc = 'M'
fem = 'F'
sexo = ''
while sexo in 'M' and sexo in 'F':
    sexo = str(input('SEXO[M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Você digitou errado!')
        novo = str(input('Digite novamente. Sexo[M/F]: '))
print('FIM')



