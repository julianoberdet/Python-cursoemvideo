#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#--Se ele ainda vai se alistar ao serviço militar;
#--Se é a hora de se alistar;
#--Se já passou o tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento? '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar \033[31mIMEDIATAMENTE\033[m!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
else:
    saldo = idade - 18
    print(f'Você ja deveria ter se alistado há {saldo} anos!')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
