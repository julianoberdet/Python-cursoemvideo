#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas
# ainda não atingiram a maioridade, e quantas ja atingiram.

from datetime import date
atual = date.today().year
for c in range(7):
    nasc = int(input('Seu ano de nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        idade = atual - nasc
        print('Já completaram a maioridade')
    elif idade < 21:
        idade = atual - nasc
        print('Não completou a maioridade')
    print(f'Você tem {idade} anos')
