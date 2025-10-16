#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo, qual é o nome do homem mais velho, quantas mulheres tem menos de 20 anos

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f"{f'{c}ª Pessoa':-^30}")
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: '))
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    somaidade += idade
    mediaidade = somaidade / 4
print(f'A média de idade do grupo é {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} e o nome dele é {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com neos de 20 anos')
