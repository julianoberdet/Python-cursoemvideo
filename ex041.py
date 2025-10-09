#A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:
'''Até 9 anos : MIRIM
Até 14 anos : INFANTIL
Até 19 anos : JUNIOR
Até 20 anos : SENIOR
Acima : MASTER'''

from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação : MIRIM')
elif idade <= 14:
    print('Classificação : INFANTIL')
elif idade <= 19:
    print('Classificação : JUNIOR')
elif idade <= 25:
    print('Classificação : SENIOR')
else:
    print('Classificação : MASTER')