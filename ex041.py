#A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:
'''Até 9 anos : MIRIM
Até 14 anos : INFANTIL
Até 19 anos : JUNIOR
Até 20 anos : SENIOR
Acima : MASTER'''

ano = int(input('Em que ano você nasceu? '))
idade = 2025 - ano
if idade <= 9:
    print(f'Você tem {idade} anos classificado como MIRIM')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos e é classificado como INFANTIL')
elif 14 <= idade <= 19:
    print(f'Você tem {idade} anos e é classificado como JUNIOR')
elif idade == 20:
    print(f'Você tem {idade} anos e é classificado como SENIOR')
else:
    print(f'Você tem {idade} anos e é classifcado como MASTER')