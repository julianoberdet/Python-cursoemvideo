maior = homem = mulhermenor = 0
Sexo = ' '
usuario = ' '
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
    usuario = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if usuario in 'Ss':
        if idade > 18:
            maior += 1
        if sexo in 'Mm':
            homem += 1
        if sexo in 'Ff':
            if idade < 20:
                mulhermenor += 1
    else:
        break
print(f'Foram cadastradas {maior} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {mulhermenor+1} mulheres com menos de 20 anos')