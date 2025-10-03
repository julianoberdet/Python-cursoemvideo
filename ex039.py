#

ano = int(input('Qual seu ano de nascimento? '))
alistar = (2025 - ano)
if alistar < 17:
    tempo = 17 - alistar
    print(f'Você tem {alistar} anos e ainda vai se alistar ao serviço militar.')
elif alistar == 17:
    print(f'Você tem {alistar} anos e está na hora de se alistar pro exército!')
    tempo = 17 - alistar
elif alistar > 18:
    print(f'Você tem {alistar} anos e já passou o tempo de alistamento.')
    tempo = 18 - alistar
print(f'Falta {tempo} ano para se alistar')