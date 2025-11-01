tot18 = totH = totM = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM += 1
    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if usuario == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é {tot18}')
print(f'Foram cadastrados {totH} homens.')
print(f'E temos {totM} mulheres com menos de 20 anos.')
