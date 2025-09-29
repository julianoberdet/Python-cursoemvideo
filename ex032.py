#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
ano = int(input('Digite um ano qualquer: Coloque 0 se quiser analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto')
else:
    print(f'O ano de {ano} não é Bissexto')