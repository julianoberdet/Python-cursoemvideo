from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Você tem {idade} anos, VOTO NEGADO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos, VOTO OPCIONAL!'
    else:
        return f'Você tem {idade} anos, VOTO OBRIGATÓRIO'


#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))